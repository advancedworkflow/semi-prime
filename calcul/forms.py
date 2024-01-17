# dwitter/forms.py

from django import forms
from .util import rabinMiller


class PrimeForm(forms.Form):
    nombre = forms.IntegerField(required=True)

    def clean(self):
        cleaned_data = super(PrimeForm, self).clean()
        nombre = self.cleaned_data.get("nombre")


        if rabinMiller(nombre) =='error':
            raise forms.ValidationError('le nombre ne peut pas etre 0 ou 1 ')
        if rabinMiller(nombre):
            raise forms.ValidationError('le nombre est premier choisissez un autre nombre')




        return cleaned_data