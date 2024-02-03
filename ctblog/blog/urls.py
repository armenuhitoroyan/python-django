from django.urls import path
from .views import home_page, contact_us

urlpatterns = [
    path('', home_page),
    path('contact-us/', contact_us)
]