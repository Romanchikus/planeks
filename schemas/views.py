from django.shortcuts import render
from django.views.generic import *
from .forms import ShemasForm
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


class SchemaCreate(SchemaParent, CreateView):

    pass
    

class SchemaEdit(SchemaParent, UpdateView):
    
    pass
    
class ColumnSchemasCreate(CreateView):

    template_name = 'home.html'
    form_class = ShemasForm
    
    
