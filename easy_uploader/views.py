from urllib import parse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from .models import File, Category
from .forms import FileForm, CategoryForm


class FileIndexView(generic.ListView):
    """ファイル一覧."""

    model = File
    queryset = File.objects.order_by('-created_at')
    paginate_by = 20


def indirect_link(request, pk):
    """間接リンク。実際のURLへリダイレクト."""
    file = get_object_or_404(File, pk=pk)
    return redirect(file.src.url)

class FileCategoryView(generic.ListView):
    """カテゴリ別のファイル一覧."""

    model = File
    paginate_by = 20
    
    def get_queryset(self):
        """カテゴリでfilter."""
        category_pk = self.kwargs['pk']
        return File.objects.filter(
            category__pk=category_pk).order_by('-created_at')



class FileCreateView(LoginRequiredMixin, generic.CreateView):
    """ファイルの作成."""

    model = File
    form_class = FileForm
    success_url = reverse_lazy("easy_uploader:file_index")


class FileUpdateView(LoginRequiredMixin, generic.UpdateView):
    """ファイルの更新."""

    model = File
    form_class = FileForm
    success_url = reverse_lazy("easy_uploader:file_index")


class FileDeleteView(LoginRequiredMixin, generic.DeleteView):
    """ファイルの削除."""

    model = File
    success_url = reverse_lazy("easy_uploader:file_index")


class CategoryIndexView(generic.ListView):
    """カテゴリの一覧."""

    model = Category
    queryset = Category.objects.order_by('-created_at')
    paginate_by = 20


class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    """カテゴリの作成."""

    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("easy_uploader:category_index")


class CategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    """カテゴリの更新."""

    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("easy_uploader:category_index")


class CategoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    """カテゴリの削除."""

    model = Category
    success_url = reverse_lazy("easy_uploader:category_index")