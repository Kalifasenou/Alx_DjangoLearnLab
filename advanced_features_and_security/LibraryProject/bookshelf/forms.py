from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(label="Votre nom", max_length=100)
    email = forms.EmailField(label="Votre e-mail")
