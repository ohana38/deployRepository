from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import UserUpdateForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
        
    return render(request, "accounts/signup.html", {"form": form})

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'accounts/user_edit.html'
    success_url = reverse_lazy('list')  

    def get_object(self):
        return self.request.user  
     
    
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('list')      

@login_required
def user_edit(request):
    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(user=request.user, data=request.POST)

        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            update_session_auth_hash(request, password_form.user)  # ログイン維持
            messages.success(request, '保存が完了しました！') 
            return redirect('user_edit')
    else:
        user_form = UserChangeForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)

    return render(request, 'accounts/user_edit.html', {
        'user_form': user_form,
        'password_form': password_form,
    })