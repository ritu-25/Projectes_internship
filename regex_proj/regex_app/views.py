from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def position(request):
    return render(request,'position.html')

def home(request):
     return render(request,'home.html')