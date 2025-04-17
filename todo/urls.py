from django.urls import path
from .views import WelcomeView, TodoDetail, TodoList, TodoCreate, TodoUpdate, TodoDelete, RegisterView
from django.contrib.auth import views as auth_views
from .views import CategoryList, CategoryCreate, CategoryUpdate, CategoryDelete
from .views import ToggleStatusView

urlpatterns = [
    path("", WelcomeView.as_view(), name="welcome"),
    path("list/", TodoList.as_view(), name="list"),
    path("detail/<int:pk>", TodoDetail.as_view(), name="detail"),
    path("create/", TodoCreate.as_view(), name="create"),
    path("update/<int:pk>", TodoUpdate.as_view(), name="update"),
    path("delete/<int:pk>", TodoDelete.as_view(), name="delete"),
    path("register/", RegisterView.as_view(), name="register"),
    path("categories/", CategoryList.as_view(), name="category_list"),
    path("categories/create/", CategoryCreate.as_view(), name="category_create"),
    path("categories/update/<int:pk>/", CategoryUpdate.as_view(), name="category_update"),
    path("categories/delete/<int:pk>/", CategoryDelete.as_view(), name="category_delete"),
    path("toggle_status/<int:pk>/", ToggleStatusView.as_view(), name="toggle_status"),
]
    # path("login/", auth_views.LoginView.as_view(), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    



    