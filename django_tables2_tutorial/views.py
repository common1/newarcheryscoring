# tutorial/views.py
from django.views.generic import ListView
from .models import Person
from .tables import PersonTable

class PersonListView(ListView):
    model = Person
    table_class = PersonTable
    template_name = 'django_tables2_tutorial/people.html'