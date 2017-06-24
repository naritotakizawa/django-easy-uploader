====================
django-easy-uploader
====================

シンプルなファイルアップローダーです。

https://torina.top/uploader

Quick start
-----------
1. インストールする::

    pip install -U https://github.com/naritotakizawa/django-easy-uploader/archive/master.tar.gz

2. settings.pyに追加する::

    INSTALLED_APPS = [
        ...
        'easy_uploader',
    ]

    # アップロードファイルのディレクトリ・URL設定
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
    
    # ログインURL
    LOGIN_URL = 'admin:login'

3. urls.pyに足す::

    url(r'^upld/', include('easy_uploader.urls', namespace="easy_uploader")),

4. python manage.py migrate　でモデルを追加する.

5. http://127.0.0.1:8000/upld/ にアクセスし、ファイルのアップロードなどを行う