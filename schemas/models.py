from django.db import models



class Schemas(models.Model):

    title = models.CharField(max_length=254)
    fields = models.JSONField()
    modified = models.DateField(auto_now=True)
    

class ColumnSchemas(models.Model):

    id = models.OneToOneField('Schemas', on_delete=models.CASCADE, primary_key=True)
    field = models.JSONField(default='dict')