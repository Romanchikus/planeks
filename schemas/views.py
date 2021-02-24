from django.shortcuts import render
from django.views.generic import *
from .forms import ColumnSchemasForm, CustomUserCreationForm
from .models import *
from django.urls import  reverse_lazy, reverse
import json  
import ast
from django.shortcuts import get_object_or_404

from django.http import  HttpResponseRedirect
from planeks.tasks import hello_world
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(LoginRequiredMixin, ListView):


    model = Schemas
    template_name = 'home.html'

    def get_queryset(self):
        schemas = Schemas.objects.filter(admin=self.request.user)
        return schemas


class SignupPageView(CreateView):
    
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class SchemaParent(LoginRequiredMixin):

    model = Schemas
    template_name = 'edit_schema.html'
    fields = ['title']
    success_url = reverse_lazy('home')
    second_form_class = ColumnSchemasForm
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        return context
    
    def form_valid(self, form):
        response = dict(self.request.POST.lists())
        if response.get('column'):
            form.instance.json_fields = self.convert_to_json(response)
        form.instance.admin = self.request.user
        form.save()
        response = super().form_valid(form)
        return response

    def convert_to_json(self, response):

        dictionary = dict()
        columns, types, ran_from , ran_from_to = (response['column'],
         response['types'], response['ran_from'], response['ran_from_to'])
        print(response)
        try:
            for i, _ in enumerate(columns):
                if columns[i] != '' and types[i] != '' :
                    dictionary[columns[i]] = [ types[i], ran_from[i] , ran_from_to[i] ]
        except IndexError:
            pass
        
        if len(dictionary) == 0:
            return 0
        print(dictionary)
        return json.dumps(dictionary)


class SchemaCreate(SchemaParent, CreateView):
    
    pass
    

class SchemaEdit( SchemaParent, UpdateView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.get_object().json_fields:
            context['json_fields'] = ast.literal_eval(self.get_object().json_fields)
        if self.object.admin != self.request.user:
            return self.handle_no_permission()
        return context
    

class SchemaDelete(LoginRequiredMixin, DeleteView):

    model = Schemas
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy("home")
    
    def get_context_data(self, **kwargs):        
        if self.object.admin != self.request.user:
            return self.handle_no_permission()
        return super().get_context_data(**kwargs)


class GenerateCsv( LoginRequiredMixin, View):

    template_name = 'generate_csv.html'

    def post(self, request, *args, **kwargs):
        pk= request.POST.get('pk')
        schemas = get_object_or_404(Schemas, pk=pk)
        if schemas.admin != self.request.user:
            return self.handle_no_permission()
        iters = request.POST.get('iters')
        gen = schemas.generatedschema_set.create()
        data = json.loads(schemas.get_json_data())
        print(data)
        hello_world.delay(title=schemas.title, date=gen.created,
            data=(data), iters=iters, pk=gen.pk)
        gen.save()

        return HttpResponseRedirect(reverse("list_csv",
                                        kwargs={'pk':pk},
                                    )
                            )


class ListCsvSchemas(LoginRequiredMixin, ListView):

    template_name = 'generate_csv.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_queryset(self):
        schemas = get_object_or_404(Schemas, pk=self.kwargs['pk'])
        if schemas.admin != self.request.user:
            return self.handle_no_permission()
        gen = schemas.generatedschema_set.all()
        return gen

    