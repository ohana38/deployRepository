from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings


class Category(models.Model):
    name = models.CharField("カテゴリ名", max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # ユーザーごとのカテゴリを関連づける
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

class Todo(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # これによりカスタムユーザーモデルを参照
        on_delete=models.CASCADE
    )
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
    priority = models.IntegerField("優先度", default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    status = models.IntegerField("状態", choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return self.title
    

    