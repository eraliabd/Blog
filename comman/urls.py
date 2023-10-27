from django.urls import path
from .views import contact, contact_info, about_info

urlpatterns = [
    path('contact_info/', contact_info, name='contact_info'),
    path('contact/', contact, name='contact'),
    path('about/', about_info, name='about_info'),
]
