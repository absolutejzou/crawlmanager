from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(max_length=32, min_length=1)
    password = forms.CharField(min_length=8, max_length=32)
