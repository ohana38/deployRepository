from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField("カテゴリ名", max_length=50)

    def __str__(self):
        return self.name

class Todo(models.Model):
    STATUS_CHOICES = [
        (0, '未完了'),
        (1, '完了'),
    ]
    PRIORITY_CHOICES = [
        (1, '低'),
        (2, '中'),
        (3, '高'),
    ]
    title = models.CharField("タスク名", max_length=30)
    description = models.TextField("詳細", blank=True)
    deadline = models.DateField("締切")
    priority = models.IntegerField("優先度", choices=PRIORITY_CHOICES, default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    status = models.IntegerField("状態", choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return self.title
    

    