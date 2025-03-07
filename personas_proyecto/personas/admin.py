from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "role", "email")
    fieldsets = [
        ("Información básica", {
            'fields': ['name', 'last_name', 'gender', 'birth_date']
        }),
        ("Detalles de contacto", {
            'fields': ['phone_number', 'email', 'address']
        }),
        ("Información adicional", {
            'fields': ['role', 'photo', 'biometric_fingerprint']
        }),
    ]