from django import forms
class SimpleForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
{'name': ['This field is required.'], 'password': ['This field is required.']}