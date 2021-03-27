from django import forms
from home.models import UserProfileInfo
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    firstname = forms.CharField(max_length=70)
    lastname = forms.CharField(max_length=70)
    class Meta():
        model = User
        fields = ('username','firstname','lastname','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')
         