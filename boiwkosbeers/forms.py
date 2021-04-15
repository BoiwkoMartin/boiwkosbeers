from django import forms
from django.forms import ModelForm

class ContactoForm(forms.Form):
	correo = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea)