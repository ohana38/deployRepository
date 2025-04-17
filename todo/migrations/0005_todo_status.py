# Generated by Django 5.2 on 2025-04-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todo_category_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.IntegerField(choices=[(0, '未完了'), (1, '完了')], default=0, verbose_name='状態'),
        ),
    ]
