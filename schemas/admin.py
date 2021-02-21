from django.contrib import admin
from .models import Schemas, GeneratedSchema



admin.site.register(Schemas)
admin.site.register(GeneratedSchema)
