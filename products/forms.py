from django import forms

class Formulario(forms.Form):
    refresco = forms.CharField(max_length=40)
    cont = forms.IntegerField()
    description = forms.CharField()