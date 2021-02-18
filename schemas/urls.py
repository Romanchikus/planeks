from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("create/", SchemaCreate.as_view(), name="create_schema"),
    path("edit/<int:pk>/", SchemaEdit.as_view(), name="edit_schema"),
    path("delete/<int:pk>/", SchemaDelete.as_view(), name="delete_schema"),

]