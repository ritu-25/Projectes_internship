from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def product(request):
    return render(request,'product.html')

def instagram(request):
    return render(request,'instagram.html')

def contact(request):
    return render(request,'contact.html')