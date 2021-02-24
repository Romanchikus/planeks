from django.db import models
import json
from django.contrib.auth.models import User

class Schemas(models.Model):

    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schema_user')
    title = models.CharField(max_length=254)
    json_fields = models.JSONField()
    modified = models.DateField(auto_now=True)

    def get_json_data(self):
        return self.json_fields


    class Meta:
        verbose_name = ("Schema")
        verbose_name_plural = ("Schemas")

    def __str__(self):
        return self.title
    
        
def content_file_name(instance, filename):
    return '/'.join(['content', filename])

class GeneratedSchema(models.Model):

    schemas = models.ForeignKey(Schemas, on_delete=models.CASCADE)
    created = models.DateField(auto_now=True)
    csv = models.FileField(upload_to=content_file_name,blank=True, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        index_together = [('created', 'schemas')]