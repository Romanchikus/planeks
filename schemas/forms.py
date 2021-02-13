from django import forms

GEEKS_CHOICES =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
) 

class ShemasForm(forms.Form):

    schema = forms.ChoiceField(choices=GEEKS_CHOICES)