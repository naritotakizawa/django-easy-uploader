from django import forms
from .models import File, Category


class FileForm(forms.ModelForm):
    """Fileモデルのフォーム."""

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
            'created_at': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),
        }


class CategoryForm(forms.ModelForm):
    """Categoryモデルのフォーム."""

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'created_at': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),
        }
