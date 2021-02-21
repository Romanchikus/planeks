from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

GEEKS_CHOICES =( 
    ("name", "Name"), 
    ("job", "Job"), 
    ("domain_name", "Domain name"), 
    ("phone_number", "Phone number"), 
    ("company", "Company name"), 
    ("text", "Text"), 
    ("random_int", "Integer"), 
    ("ascii_email", "Email"), 
    ("address", "Address"), 
    ("date_time", "Date"),
) 

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)

class ColumnSchemasForm(forms.Form):

    column = forms.CharField(max_length=254)
    types = forms.ChoiceField(choices=GEEKS_CHOICES)