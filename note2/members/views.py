from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class = UserChangeForm
    template_name = 'register.html'
    success_url = reverse_lazy('log')
