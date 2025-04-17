from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import UserUpdateView
from .views import CustomPasswordChangeView
from .views import user_edit

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html',next_page='/'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('edit/', UserUpdateView.as_view(), name='edit_user'), 
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('edit/', user_edit, name='user_edit'),
]
