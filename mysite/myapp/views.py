from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from .models import Person
from .forms import PersonForm

# Create your views here.
def person_list_view(request):
    context = {}

    context["person_list"] = Person.objects.all()
    print(Person.objects.all())
    
    return render(request, "myapp/person.html", context)


class PersonListView(ListView):
    model = Person
    paginate_by = 100
    template_name = "myapp/person.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now
        return context
    

class PersonDetailView(DetailView):
    model = Person
    template_name = "myapp/person_detail.html"


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = "myapp/person_create.html"
    success_url = "/"


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = "myapp/person_update.html"
    success_url = "/"
    

class PersonDeleteView(DeleteView):
    model = Person
    template_name = "myapp/person_delete.html"
    success_url = "/"


"""
    Views are like controllers
    'CreateView' - A view that displays a form for creating an object, redisplaying the form with validation errors (if there are any) and saving the object.
    'DeleteView' - A view that displays a confirmation page and deletes an existing object. 
    'DetailView' - A view for a specific object based on its ID
    'ListView' - Show a list/array of objects in a View
    'UpdateView' - A view that displays a form for updating an object, redisplaying the form with validation errors (if there are any) and saving the object.
"""