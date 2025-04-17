from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "deadline", "priority", "category"]
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'priority': forms.Select(choices=Todo.PRIORITY_CHOICES),
        }
        
