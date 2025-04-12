from django import forms
from .models import Todo, Category

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "deadline", "priority", "category"]
