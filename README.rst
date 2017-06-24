====================
django-easy-uploader
====================

.. image:: https://travis-ci.org/naritotakizawa/django-easy-uploader.svg?branch=master
    :target: https://travis-ci.org/naritotakizawa/django-easy-uploader

.. image:: https://coveralls.io/repos/github/naritotakizawa/django-easy-uploader/badge.svg?branch=master
    :target: https://coveralls.io/github/naritotakizawa/django-easy-uploader?branch=master



シンプルなファイルアップローダーです。

https://torina.top/uploader

Requirement
--------------

:Python: 3.5以上
:Django: 1.10以上


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