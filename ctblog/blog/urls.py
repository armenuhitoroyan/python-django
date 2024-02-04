from django.urls import path
from .views import home_page, contact_us, blog_detail

urlpatterns = [
    path('', home_page),
    path('contact-us/', contact_us),
    path('blog-detail/<int:pk>/', blog_detail),  # pk primary key == id
]