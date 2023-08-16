
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from .models import Person

# Create your views here.


class PersonListView(ListView):
    model = Person
    context_object_name = "person_list"
    paginate_by = 2

class PersonDetailView(DetailView):
    model = Person
    context_object_name = "person_detail"