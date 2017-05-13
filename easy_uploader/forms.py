from django import forms
from .models import Img, File, Category


class ImgForm(forms.ModelForm):

    class Meta:
        model = Img
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
        }


class FileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
            'category': forms.Select(attrs={
                'class': "form-control",
            }),
        }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
            }),
        }
