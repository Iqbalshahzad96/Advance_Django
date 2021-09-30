from django.views.generic import (  TemplateView, ListView, 
                                    DetailView,CreateView,
                                    UpdateView, DeleteView)
from . import models
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class schoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdaateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
