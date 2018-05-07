from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.views import generic

# Create your views here.

class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('success')
    template_name = 'accounts/signup.html'

