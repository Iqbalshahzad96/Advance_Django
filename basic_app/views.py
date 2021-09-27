from django.shortcuts import redirect, render
from django.views.generic import View, TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
