from collections import defaultdict
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django import forms
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category
from django.views.generic import TemplateView
from django.views import View
from accounts.forms import CustomUserCreationForm

class WelcomeView(TemplateView):
    template_name = "todo/welcome.html" 
  
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('list')  
        return super().dispatch(request, *args, **kwargs)

class TodoList(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = "tasks"
    login_url = "login"  
    
    def get_queryset(self):
        sort_by = self.request.GET.get("sort", "deadline")
        return Todo.objects.filter(user=self.request.user).order_by(sort_by)

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'deadline', 'priority', 'category']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'priority': forms.Select(choices=Todo.PRIORITY_CHOICES),
        }

class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"    
    
class TodoCreate(LoginRequiredMixin,CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("list")  
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # ←ここでログインユーザーをセット！
        return super().form_valid(form)  
    
class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("list")   
    
class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")   
    

class CategoryList(ListView):
    model = Category
    context_object_name = "categories"

class CategoryCreate(CreateView):
    model = Category
    fields = ["name"]
    success_url = reverse_lazy("category_list")

class CategoryUpdate(UpdateView):
    model = Category
    fields = ["name"]
    success_url = reverse_lazy("category_list")

class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy("category_list")
    
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'todo/register.html'
    success_url = reverse_lazy('login')  
    
    def form_valid(self, form):
        # フォームが有効な場合、ユーザーを作成
        response = super().form_valid(form)
        # 必要に応じて他の操作を行うことができます（例：メール送信など）
        return response

    def form_invalid(self, form):
        # フォームが無効な場合、エラーメッセージを表示
        return self.render_to_response(self.get_context_data(form=form))
  
      
@login_required
def todo_list(request):
    sort = request.GET.get('sort')
    tasks = Todo.objects.filter(user=request.user)
    
    if sort == 'deadline':
        tasks = tasks.order_by('deadline')
    elif sort == 'priority':
        tasks = tasks.order_by('priority')
        
    grouped_tasks = defaultdict(list)
    for task in tasks:
        grouped_tasks[task.category.name if task.category else '未分類'].append(task)
    
    return render(request, 'todo/todo_list.html', {
        'grouped_tasks': grouped_tasks.items()
    })

class ToggleStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Todo, pk=pk)
        task.status = 0 if task.status == 1 else 1
        task.save()
        return redirect('list')    