# Contact Book API

A simple Contact Book API built with Django REST Framework, using ViewSets and Routers 
to provide full CRUD functionality. Authentication is handled using JWT (JSON Web Tokens) 
via djangorestframework-simplejwt.


# SETUP

# Clone project
git clone <your-repo-url>
cd <project-folder>

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser


# AUTHENTICATION (JWT)

Add this to your project-level urls.py:

from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/', include('contacts.urls')),  # your contact routes
    path('api/access_token/', TokenObtainPairView.as_view(), name='access_token'),
    path('api/refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
]

Endpoints:
- POST /api/access_token/ → Obtain access & refresh tokens
- POST /api/refresh_token/ → Refresh access token

Header for protected requests:
Authorization: Bearer <your_access_token>


# CONTACT API ENDPOINTS

Registered via DRF Router:

Method   Endpoint            Description
GET      api/contacts/           List all user contacts
POST     api/contacts/           Create a new contact
GET      api/contacts/{id}/      Retrieve a contact
PUT      api/contacts/{id}/      Update a contact
DELETE   api/contacts/{id}/      Delete a contact

Note: Each user can only see and manage the contacts they created.


# RUN SERVER


python manage.py runserver
