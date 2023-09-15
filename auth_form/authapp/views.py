from django.shortcuts import render,HttpResponse,redirect
from .forms import register_form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login , logout

# Create your views here.
def auth(request):
    if request.method == "POST":
        data = register_form(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('data saved !!..')
    data = register_form()
    return render(request,'index.html',{'data':data})



# Create Account
def create_account(request):
    if request.method == "POST":
        x= register_form(request.POST)
        
        if x.is_valid():
            x.save()
            return HttpResponse('Data Saved !!...')
    x = register_form()
    my_dict ={
        'x':x
    }
    return render(request,'account.html',my_dict)


# Create Login
def login_form(request):
    if request.method == "POST":
        x = AuthenticationForm(data = request.POST)
        print('>>>>x',x)
        if x.is_valid():
            uname = x.cleaned_data['username']
            passw = x.cleaned_data['password']
            user = authenticate(username = uname,password = passw)
            # return HttpResponse('You are logined successfully !!...')
            
            if user is not None:
                login(request,user)
                return redirect('/get')
            
    x = AuthenticationForm()
    context = {
        'x':x
    }
    return render(request, 'login_form.html',context)


# Logout Form 
def get_out(request):
    logout(request)
    return redirect('/login')
    