from django.shortcuts import render, HttpResponse
from .models import Blog, Contact

# Create your views here.

def home_page(request):

    context = {}
    blogs = Blog.objects.all()
    context["blogs"] = blogs
    # return HttpResponse("Welcome to CT Blog!")
    return render(request, "home.html", context)

def contact_us(request):

    if request.POST:
       new_contact = Contact.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            message = request.POST['message']
        )
    # return HttpResponse("Welcome to Contact Us page!")
    return render(request, "contact_us.html", {})

def blog_detail(request, pk):  # pk for details' id
    context = {}
    blog = Blog.objects.get(id=pk)
    context["blog"] = blog

    return render(request, "blog_detail.html", context)