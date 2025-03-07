from django.db import models
from django.utils.translation import gettext_lazy as _

class Person(models.Model):
    name = models.CharField(_("Nombre"), max_length=100)
    last_name = models.CharField(_("Apellido"), max_length=100)
    gender = models.CharField(_("Sexo"), max_length=10, null=True)
    birth_date = models.DateField(_("Fecha de nacimiento"), null=True)
    phone_number = models.CharField(_("Número de teléfono"), max_length=15, null=True)
    email = models.CharField(_("Email"), max_length=100, null=True)
    role = models.CharField(_("Rol"), max_length=50, null=True)
    photo = models.ImageField(_("Foto"), upload_to='photos/', blank=True, null=True)
    biometric_fingerprint = models.FileField(upload_to='biometrics/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # La clase Meta DEBE estar indentada dentro de Person
    class Meta:
        verbose_name = _("Persona")
        verbose_name_plural = _("Personas")

    # El método __str__ también debe estar correctamente indentado
    def __str__(self):
        return f"{self.name} {self.last_name}"