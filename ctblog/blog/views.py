from django.shortcuts import render, HttpResponse

# Create your views here.

def home_page(request):
    # return HttpResponse("Welcome to CT Blog!")
    return render(request, "home.html", {})

def contact_us(request):
    # return HttpResponse("Welcome to Contact Us page!")
    return render(request, "contact_us.html", {})