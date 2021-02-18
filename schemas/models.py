from django.db import models
import json


class Schemas(models.Model):

    title = models.CharField(max_length=254)
    json_fields = models.JSONField(default={})
    modified = models.DateField(auto_now=True)

    def get_json_data(self):
        return self.json_fields

    def __str__(self):
        return self.title
    
        
    

class ColumnSchemas(models.Model):

    id = models.OneToOneField('Schemas', on_delete=models.CASCADE, primary_key=True)
    field = models.JSONField(default='dict')