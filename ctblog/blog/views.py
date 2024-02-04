from django.shortcuts import render, HttpResponse
from .models import Blog

# Create your views here.

def home_page(request):

    context = {}
    blogs = Blog.objects.all()
    context["blogs"] = blogs
    # return HttpResponse("Welcome to CT Blog!")
    return render(request, "home.html", context)

def contact_us(request):
    # return HttpResponse("Welcome to Contact Us page!")
    return render(request, "contact_us.html", {})

def blog_detail(request, pk):  # pk for details' id
    context = {}
    blog = Blog.objects.get(id=pk)
    context["blog"] = blog

    return render(request, "blog_detail.html", context)