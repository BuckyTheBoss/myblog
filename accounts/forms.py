from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils import timezone



class MyAuthenticationForm(AuthenticationForm):
    date = forms.DateTimeField(initial=timezone.now())
    field_order = ['date', 'password', 'username']

