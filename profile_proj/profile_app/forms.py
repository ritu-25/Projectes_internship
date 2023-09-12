from django import forms 

class profile_form(forms.Form):
    name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Name'}))
    fathername = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Fathername'}))
    mothername = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Mothername'}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email'}))
    roll_no = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your Roll_no'}))
    stream = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Steram'}))
    address = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Address'}))
    state = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your State'}))
    city = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your City'}))
    pin_code = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your Pin_code'}))
    gender =forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Gender'}))
    mobile_no =forms.CharField(max_length=10,required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your Mobile No.'}))
    image =forms.ImageField(required=True,widget=forms.FileInput(attrs={'class':'form-control'}))
    description = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Anything here'}))
    