from django import forms 
# from .models import student

# class student_forms(forms.ModelForm):
    
#     class Meta:
#         model = student
#         fields = ('_all_')




class myform(forms.Form):
       name = forms.CharField()
       email = forms.EmailField()
       address = forms.CharField()