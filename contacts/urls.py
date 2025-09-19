from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contacts', views.ContactViewSet, basename='contact' )

urlpatterns = [
    path('', include(router.urls)),
]