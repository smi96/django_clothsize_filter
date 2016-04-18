from django import forms

from .models import Product, Product_Varients, Sno

class ChoiceForm(forms.Form):
    CHOICES = (('Xtra-Small','Xtra-Small'),
               ('Small','Small'),
               ('Medium','Medium'),
               ('Large','Large'),
               ('Xtra-Large','Xtra-Large'),	)
    choices_picked = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    