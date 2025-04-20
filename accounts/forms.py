from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']  # 必要な項目だけ
        
class CustomPasswordChangeForm(PasswordChangeForm):
    pass