from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = 'username', max_length = 150)
    subdomain = forms.CharField(label = 'subdomain', max_length = 150)
    password = forms.CharField(label = 'password', max_length = 256)