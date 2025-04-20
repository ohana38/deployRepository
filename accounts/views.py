from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

# --- ユーザー名変更用フォーム ---
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']  # 必要なフィールドだけ


# --- カスタムログインビュー ---
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    
    def form_valid(self, form):
        current_user = self.request.user
        new_user = form.get_user()
        if current_user.is_authenticated and current_user != new_user:
            messages.error(self.request, 'すでに別のユーザーでログイン中です。')
            return redirect('error_403')  # 作成済みの403エラーページにリダイレクト
        auth_login(self.request, new_user)
        return redirect(self.get_success_url())


# --- ユーザー情報とパスワード変更ビュー ---
class UserEditView(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)
        return render(request, 'accounts/user_edit.html', {  # ← パス修正済み！
            'user_form': user_form,
            'password_form': password_form,
        })

    def post(self, request):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(user=request.user, data=request.POST)

        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, '保存完了')
            return redirect('user_edit')

        return render(request, 'accounts/user_edit.html', {  # ← こちらも修正済み！
            'user_form': user_form,
            'password_form': password_form,
        })
