from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)  # Puedes cambiar a ForeignKey si defines un modelo de categoría
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    biometric_fingerprint = models.FileField(upload_to='biometrics/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
