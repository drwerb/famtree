from django.contrib import admin

from .models import Person, PersonInfo
# Register your models here.

admin.site.register(Person)
admin.site.register(PersonInfo)
