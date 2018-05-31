from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.views import generic
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.

class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('success')
    template_name = 'accounts/signup_temp.html'
