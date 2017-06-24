from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('easy_uploader.urls')),
]
