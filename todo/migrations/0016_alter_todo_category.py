# Generated by Django 4.2.1 on 2023-05-25 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0015_alter_todo_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(default='あ', on_delete=django.db.models.deletion.PROTECT, to='todo.category', verbose_name='カテゴリ'),
        ),
    ]
