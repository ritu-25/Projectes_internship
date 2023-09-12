from django.shortcuts import render , HttpResponse
from .models import myprofile
from .forms import profile_form

# Create your views here.
def profile(request):
    if request.method == "POST":
     name = request.POST['n_ame']
     f_name = request.POST['fathername']
     m_name = request.POST['mothername']
     email = request.POST['email']
     roll_no = request.POST['number']
     stream = request.POST['Stream']
     address = request.POST['inputAddress']
     state = request.POST['State']
     city = request.POST['City']
     gender = request.POST['gender']
     pin_code = request.POST['number']
     mobile_number = request.POST['mobile']
     image = request.POST['image']
     descripation = request.POST['description']
     
     myprofile(name=name,fathername=f_name,mothername=m_name,email=email,roll_no=roll_no,stream=stream,address=address,state=state,city=city,gender=gender,pin_code=pin_code,mobile_no=mobile_number,image=image,description=descripation).save()
     
     print(name,f_name,m_name,email,roll_no,stream,address,state,city,gender,pin_code,mobile_number,image,descripation)
       
     
    return render(request,'profile.html')


def my_form(request):
    if request.method == "POST":
        a = profile_form(request.POST,request.FILES)
        print(a)

        if a.is_valid():
            p = a.cleaned_data['name']
            b =a.cleaned_data['fathername']
            c = a.cleaned_data['mothername']
            d =a.cleaned_data['email']
            e =a.cleaned_data['roll_no']
            f =a.cleaned_data['stream']
            g =a.cleaned_data['address']
            h =a.cleaned_data['state']
            i =a.cleaned_data['city']
            j =a.cleaned_data['pin_code']
            k=a.cleaned_data['gender']
            l=a.cleaned_data['mobile_no']
            m  = a.cleaned_data['image']
            o =a.cleaned_data['description']
            
            myprofile(name=p,fathername=b,mothername=c,email=d,roll_no=e,stream=f,address=g,state=h,city=i,gender=k,pin_code=j,mobile_no= l,image=m,description=o).save()
     
            print(p,b,c,d,e,f,g,h,i,j,k,l,m,o)
            
            return HttpResponse('Data Saved !!!...') # for return a string
    a = profile_form()
        
    context ={
        'a':a
    }
    return render(request,'form.html',context)

def get_data(request):
    data = myprofile.objects.all()
    # skill = []
    # for i in data:
    #     skill = i.skills.split(',')
    context = {
            'data':data
            # 'skill':skill
        }
    return render(request, 'content.html',context)
    

    
        