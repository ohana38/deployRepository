from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']  # 必要な項目だけ
        labels = {
            'username': 'ユーザー名',
            'first_name': '名',
            'last_name': '姓',
            # 'email': 'メールアドレス',
        }
        
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
