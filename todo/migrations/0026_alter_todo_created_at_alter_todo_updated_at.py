# Generated by Django 4.2.1 on 2023-05-29 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0025_todo_created_at_todo_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
    ]
