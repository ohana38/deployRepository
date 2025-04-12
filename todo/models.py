from django.db import models

class Category(models.Model):
    name = models.CharField("カテゴリ名", max_length=50)

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField("タスク名", max_length=30)
    description = models.TextField("詳細", blank=True)
    deadline = models.DateField("締切")
    priority = models.IntegerField("優先度", default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.title
    

    