from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    # groupsとuser_permissionsに関連名を追加
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # ここで関連名を指定
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # ここで関連名を指定
        blank=True
    )
