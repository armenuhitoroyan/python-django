from django.shortcuts import render, HttpResponse
from .models import Blog, Contact
from .forms import ContactForm, CommentForm

# Create your views here.

def home_page(request):

    context = {}
    blogs = Blog.objects.all()
    context["blogs"] = blogs
    # return HttpResponse("Welcome to CT Blog!")
    return render(request, "home.html", context)

def contact_us(request):

    context = {}
    if request.POST:
       my_form = ContactForm(request.POST)
       if my_form.is_valid():
           my_form.save()
       else:
           context["errors"] = my_form.errors
    # return HttpResponse("Welcome to Contact Us page!")
    return render(request, "contact_us.html", context)

def blog_detail(request, pk):  # pk for details' id
    context = {}
    blog = Blog.objects.get(id=pk)
    context["blog"] = blog

    if request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            obj = comment_form.save(commit=False)
            obj.blog = context["blog"]
            obj.save()
        else:
            context["errors"] = comment_form.errors

    return render(request, "blog_detail.html", context)