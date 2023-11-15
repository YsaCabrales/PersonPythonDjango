from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.utils import timezone
from .models import Person

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
    
"""
    Views are like controllers
    'CreateView' - A view that displays a form for creating an object, redisplaying the form with validation errors (if there are any) and saving the object.
    'DeleteView' - A view that displays a confirmation page and deletes an existing object. 
    'DetailView' - A view for a specific object based on its ID
    'ListView' - Show a list/array of objects in a View
    'UpdateView' - A view that displays a form for updating an object, redisplaying the form with validation errors (if there are any) and saving the object.
"""