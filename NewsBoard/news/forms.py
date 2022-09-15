from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, HiddenInput, CharField, Textarea, ImageField, MultipleChoiceField
from django.utils.translation import gettext_lazy as _
from .models import Post

from django.contrib.auth.models import Group
from django import forms


class PostForm(ModelForm):



    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'categories', 'author']

        labels = {
            'categories': _('Категория'),
            'content': _('Объявление'),
            'image': _('Изображение')
        }


