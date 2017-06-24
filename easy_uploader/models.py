import os
from django.db import models
from django.utils import timezone


class Category(models.Model):
    """カテゴリ."""
    name = models.CharField('カテゴリ名', max_length=255)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name


def get_upload_to(instance, filename):
    """upload_toを動的に指定する."""
    try:
        path = os.path.join(str(instance.category.name), filename)
    except:
        path = os.path.join('default', filename)
    return path


def default_category():
    """デフォルトのカテゴリを返す（まだなければ作る）."""
    category, _ = Category.objects.get_or_create(name='default')
    return category


class File(models.Model):
    """アップロードするファイル."""

    title = models.CharField('タイトル', max_length=255, blank=True)
    category = models.ForeignKey(
        Category, verbose_name='カテゴリ', on_delete=models.PROTECT,
        default=default_category,
    )
    src = models.FileField('ファイル', upload_to=get_upload_to)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.title

    def get_filename(self):
        """ファイル名を返す関数"""
        return os.path.basename(self.src.name)
