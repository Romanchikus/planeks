from django.shortcuts import render
from django.views.generic import *
from .forms import ColumnSchemasForm
from .models import *
from django.urls import  reverse_lazy
import json  

class HomePage(ListView):

    model = Schemas
    template_name = 'home.html'

class SchemaParent():

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
        form.instance.fields = self.convert_to_json(response)
        form.save()
        return super().form_valid(form)

    def convert_to_json(self, response):

        dictionary = dict()
        columns, types = response['column'], response['types']
        for i, _ in enumerate(columns):
            if columns[i] != '' and types[i] != '' :
                dictionary[columns[i]] = types[i]
        
        if len(dictionary) == 0:
            return 0
        return json.dumps(dictionary)


class SchemaCreate(SchemaParent, CreateView):

    pass
    

class SchemaEdit(SchemaParent, UpdateView):
    
    pass