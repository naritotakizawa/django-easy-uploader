import os
from django.db import models


class Img(models.Model):
    """アップロードするイメージ"""

    title = models.CharField("タイトル", max_length=255, blank=True)
    file = models.ImageField("ファイル", upload_to='images/', )
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.title

    def get_filename(self):
        """ファイル名を返す関数"""

        return os.path.basename(self.file.name)


class Category(models.Model):
    name = models.CharField("カテゴリ名", max_length=255)
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.name


def get_upload_to(instance, filename):
    """upload_toを動的に指定する"""

    return os.path.join(str(instance.category.name), filename)


class File(models.Model):
    """アップロードするファイル"""

    title = models.CharField("タイトル", max_length=255, blank=True)
    category = models.ForeignKey(Category, verbose_name="カテゴリ", on_delete=models.PROTECT)
    file = models.FileField("ファイル", upload_to=get_upload_to)
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.title

    def get_filename(self):
        """ファイル名を返す関数"""

        return os.path.basename(self.file.name)
