# Generated by Django 4.2.1 on 2023-05-24 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_alter_todo_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='ステータス名')),
            ],
        ),
    ]