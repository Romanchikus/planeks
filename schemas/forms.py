from django import forms

GEEKS_CHOICES =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
) 

class ColumnSchemasForm(forms.Form):

    column = forms.CharField(max_length=254)
    types = forms.ChoiceField(choices=GEEKS_CHOICES)
    extra_field_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)
        
        super(ColumnSchemasForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields
        self.fields["extra_field_count"].label= ''

        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['column_name_{index}'.format(index=index)] = \
                forms.CharField()
            self.fields['column_types_{index}'.format(index=index)] = \
                forms.CharField()
            