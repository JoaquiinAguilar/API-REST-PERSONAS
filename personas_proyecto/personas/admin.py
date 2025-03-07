from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Información básica", {
            'fields': ['name', 'last_name', 'birth_date']
        }),
        ("Detalles adicionales", {
            'fields': ['email', 'role', 'photo']
        }),
    ]
