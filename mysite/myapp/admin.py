from django.contrib import admin
from myapp.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # pass means dont do anything
    pass