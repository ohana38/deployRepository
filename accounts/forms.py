from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # 必要な項目だけ
        
class CustomPasswordChangeForm(PasswordChangeForm):
    pass

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='必須フィールドです。')

    class Meta:
        model = User
        fields = ("username", "email")  

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("このメールアドレスはすでに使われています。")
        return email
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = "8文字以上で、数字や特殊文字を含むとより強力です。"

# パスワードバリデータのエラーメッセージを日本語にカスタマイズ
from django.contrib.auth.password_validation import MinimumLengthValidator
from django.utils.translation import gettext_lazy as _

class CustomMinimumLengthValidator(MinimumLengthValidator):
    def __init__(self, *args, **kwargs):
        # パスワードが短すぎる場合のエラーメッセージを日本語に変更
        self.message = _('このパスワードは短すぎます。少なくとも8文字以上必要です。')
        super().__init__(*args, **kwargs)