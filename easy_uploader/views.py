from urllib import parse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Img, File, Category
from .forms import ImgForm, FileForm, CategoryForm


class TopPageView(generic.TemplateView):
    template_name = "easy_uploader/index.html"


class ImgIndexView(generic.ListView):
    model = Img
    queryset = Img.objects.order_by('-created_at')
    paginate_by = 20


class ImgCreateView(LoginRequiredMixin, generic.CreateView):
    model = Img
    form_class = ImgForm
    success_url = reverse_lazy("easy_uploader:img_index")


class ImgUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Img
    form_class = ImgForm
    success_url = reverse_lazy("easy_uploader:img_index")


class ImgDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Img
    success_url = reverse_lazy("easy_uploader:img_index")


class FileIndexView(generic.ListView):
    model = File
    queryset = File.objects.order_by('-created_at')
    paginate_by = 20


class FileCreateView(LoginRequiredMixin, generic.CreateView):
    model = File
    form_class = FileForm
    success_url = reverse_lazy("easy_uploader:file_index")


class FileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = File
    form_class = FileForm
    success_url = reverse_lazy("easy_uploader:file_index")


class FileDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = File
    success_url = reverse_lazy("easy_uploader:file_index")


@require_POST
@csrf_exempt
def img_api(request):
    """ 画像アップロード用のAPI

        # サンプルコード
        import requests


        url = "http://torina.top/uploader/api/image/"
        files = {'upload_file': open("test.png", "rb")}
        res = requests.post(url, files=files)
        print(res.text)
    """

    upload_file = request.FILES["upload_file"]
    image_data = Img(title="from api", file=upload_file)
    image_data.save()
    parse_url = parse.urlparse(request.build_absolute_uri())
    parse_url = parse_url._replace(path=image_data.file.url)
    url = parse.urlunparse(parse_url)
    return HttpResponse(url, content_type="text/plain")


class CategoryIndexView(generic.ListView):
    model = Category


class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("easy_uploader:category_index")


class CategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("easy_uploader:category_index")


class CategoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Category
    success_url = reverse_lazy("easy_uploader:category_index")