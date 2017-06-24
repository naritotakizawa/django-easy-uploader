from django.conf.urls import url
from . import views

app_name = 'easy_uploader'

urlpatterns = [
    # FileのCRUD
    url(r'^$', views.FileIndexView.as_view(), name='file_index'),
    url(r'^file/category/(?P<pk>[0-9]+)/$', views.FileCategoryView.as_view(), name='file_category'),
    url(r'^file/create/$', views.FileCreateView.as_view(), name='file_create'),
    url(r'^file/update/(?P<pk>[0-9]+)/$',
        views.FileUpdateView.as_view(), name='file_update'),
    url(r'^file/delete/(?P<pk>[0-9]+)/$',
        views.FileDeleteView.as_view(), name='file_delete'),
    
    # 間接リンク
    url(r'^indirect/link/(?P<pk>[0-9]+)/$',
        views.indirect_link, name='indirect_link'),

    # CategoryのCRUD
    url(r'^category/$', views.CategoryIndexView.as_view(), name='category_index'),
    url(r'^category/create/$', views.CategoryCreateView.as_view(), name='category_create'),
    url(r'^category/update/(?P<pk>[0-9]+)/$',
        views.CategoryUpdateView.as_view(), name='category_update'),
    url(r'^category/delete/(?P<pk>[0-9]+)/$',
        views.CategoryDeleteView.as_view(), name='category_delete'),
]
