from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
  
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        "this methods gets the contacts related to a user "
        return Contact.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        "this method saves the contact to the logged-in user as the owner "
        serializer.save(owner=self.request.user)