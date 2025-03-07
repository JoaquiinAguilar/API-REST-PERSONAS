from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Person
from .serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    search_fields = ['name', 'last_name', 'role']
    filter_backends = [filters.SearchFilter]

def index(request):
    return render(request, 'personas/index.html')
