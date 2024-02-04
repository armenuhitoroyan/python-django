from django.urls import path
# from .views import home_page, contact_us, blog_detail
from .views import home_page, contact_us, blog_detail
from django.conf.urls.static import static
from django.conf import settings


app_name = "blog"

urlpatterns = [
    path('', home_page, name='home'),
    path('contact-us/', contact_us, name='contact-us'),
    path('blog-detail/<int:pk>/', blog_detail, name='blog-detail'),  # pk primary key == id
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)