from django.contrib import admin
from .models import Todo, Reply, Status, Category

admin.site.register(Status)
admin.site.register(Todo)
admin.site.register(Reply)
admin.site.register(Category)
