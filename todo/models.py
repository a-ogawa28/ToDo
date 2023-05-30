from django.db import models
from django.utils import timezone


# 進捗状況
class Status(models.Model):
    # 名前の重複なし
    status_name = models.CharField('ステータス名', max_length=50, unique=True)

    def __str__(self):
        return self.status_name


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Todo(models.Model):
    title      = models.CharField('ToDo名', max_length=50)
    status     = models.ForeignKey(Status, verbose_name='進捗状況', on_delete=models.PROTECT, default=1)
    deadline   = models.DateTimeField('締め切り', null=True, blank=True)
    content    = models.TextField('内容説明', null=True, blank=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    category   = models.ForeignKey(Category, verbose_name='カテゴリ', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Reply(models.Model):
    comment    = models.TextField('コメント')
    created_at = models.DateTimeField('投稿日', default=timezone.now)
    target     = models.ForeignKey(Todo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.comment
