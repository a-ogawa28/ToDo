# Generated by Django 4.2.1 on 2023-05-24 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_alter_todo_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='category_name',
            new_name='status_name',
        ),
    ]