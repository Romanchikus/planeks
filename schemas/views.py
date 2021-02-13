from django.shortcuts import render
from django.views.generic import *
from .forms import ColumnSchemasForm
from .models import *
from django.urls import  reverse_lazy

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

        print(self.request.POST.values)
        return super().form_valid(form)


class SchemaCreate(SchemaParent, CreateView):

    pass
    

class SchemaEdit(SchemaParent, UpdateView):
    
    pass

    
    
class ColumnSchemasCreate(CreateView):

    template_name = 'home.html'
    form_class = ColumnSchemasForm
    
    
    
