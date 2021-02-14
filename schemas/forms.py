from django import forms

GEEKS_CHOICES =( 
    ("int", "Integer"), 
    ("float", "Float"), 
    ("date", "Date"), 
    ("email", "Email"), 
    ("str", "String"), 
) 

class ColumnSchemasForm(forms.Form):

    column = forms.CharField(max_length=254)
    types = forms.ChoiceField(choices=GEEKS_CHOICES)