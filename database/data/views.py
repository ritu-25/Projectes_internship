from django.shortcuts import render,HttpResponse
# from .models import student
# from .forms import student_forms
from .forms import myform

# Create your views here.
# def index(request):
#     data = student.objects.all()

#     for i in data:
#         print(i)
#     print(data)
#     context={
#         'd':data
#     }
#     return render(request,'index.html',context)



def my_form(request):
    a = myform()
    
    context ={
         'a':a
     }
    return render(request,'forms.html',context)