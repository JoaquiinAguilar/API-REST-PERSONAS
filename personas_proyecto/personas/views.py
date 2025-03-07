from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAdminUser

from .models import Person
from .serializers import PersonSerializer

# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.SearchFilter]

    search_fields = ['name', 'category']

from django.shortcuts import render

def index(request):
    return render(request, 'personas/index.html')
