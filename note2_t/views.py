from django.shortcuts import render
from django.views.generic import ListView
from .models import QuillPost



class HomeView(ListView):

    model = QuillPost
    template_name = 'home.html'