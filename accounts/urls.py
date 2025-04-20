from django.urls import path
from .views import CustomLoginView, UserEditView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('user/edit/', UserEditView.as_view(), name='user_edit'),
]
