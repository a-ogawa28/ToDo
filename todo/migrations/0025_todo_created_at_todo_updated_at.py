# Generated by Django 4.2.1 on 2023-05-29 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0024_alter_todo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='作成日時'),
        ),
        migrations.AddField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時'),
        ),
    ]
