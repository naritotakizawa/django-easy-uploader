from django.conf.urls import url
from . import views

app_name = 'easy_uploader'

urlpatterns = [
    url(r'^$', views.TopPageView.as_view(), name='index'),

    url(r'^img/$', views.ImgIndexView.as_view(), name='img_index'),
    url(r'^img/create/$', views.ImgCreateView.as_view(), name='img_create'),
    url(r'^img/update/(?P<pk>[0-9]+)/$',
        views.ImgUpdateView.as_view(), name='img_update'),
    url(r'^img/delete/(?P<pk>[0-9]+)/$',
        views.ImgDeleteView.as_view(), name='img_delete'),
    url(r'^img/api/$', views.img_api, name='img_api'),

    url(r'^file/$', views.FileIndexView.as_view(), name='file_index'),
    url(r'^file/create/$', views.FileCreateView.as_view(), name='file_create'),
    url(r'^file/update/(?P<pk>[0-9]+)/$',
        views.FileUpdateView.as_view(), name='file_update'),
    url(r'^file/delete/(?P<pk>[0-9]+)/$',
        views.FileDeleteView.as_view(), name='file_delete'),

    url(r'^category/$', views.CategoryIndexView.as_view(), name='category_index'),
    url(r'^category/create/$', views.CategoryCreateView.as_view(), name='category_create'),
    url(r'^category/update/(?P<pk>[0-9]+)/$',
        views.CategoryUpdateView.as_view(), name='category_update'),
    url(r'^category/delete/(?P<pk>[0-9]+)/$',
        views.CategoryDeleteView.as_view(), name='category_delete'),
]
