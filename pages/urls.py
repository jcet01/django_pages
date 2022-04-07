# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, ContactusView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('contactus/', ContactusView.as_view(), name='contactus'),
]
