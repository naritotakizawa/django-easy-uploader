====================
django-easy-uploader
====================

シンプルなファイルアップローダーです。
https://torina.top/uploader

Quick start
-----------
1. インストールする::

    pip install -U hg+https://bitbucket.org/toritoritorina/django-easy-uploader

2. settings.pyのINSTALLED_APPSに足す::

    INSTALLED_APPS = [
        ...
        'easy_uploader',
    ]

3. urls.pyに足す::

    url(r'^upld/', include('easy_uploader.urls', namespace="easy_uploader")),

3. python manage.py migrate　でモデルを追加する.

4. http://127.0.0.1:8000/upld/ にアクセスし、ファイルのアップロードなどを行う