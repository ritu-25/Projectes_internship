from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request,'home.html')
def about(request):
     return render(request,'about.html')
def project(request):
     return render(request,'project.html')
def contact(request):
     return render(request,'contact.html')
def profile(request):
     return render(request,'profile.html')