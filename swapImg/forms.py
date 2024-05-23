from django import forms
from .models import *
  
class UserInfoForm(forms.ModelForm):
  
    class Meta:
        model = UserInfo
        fields = ['userName', 'userAvatar', 'userAnimeAvatar' ]

