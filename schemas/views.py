from django.shortcuts import render
from django.views.generic import *
from .forms import ShemasForm
from .models import *

class HomePage(ListView):

    model = Schemas
    template_name = 'home.html'

class SchemaCreate(CreateView):

    model = Schemas
    template_name = 'home.html'
    
class ColumnSchemasCreate(CreateView):

    template_name = 'home.html'
    form_class = ShemasForm
    
    
