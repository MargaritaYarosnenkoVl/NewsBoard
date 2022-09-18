
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'categories', 'author']

        labels = {
            'title': _('Заголовок'),
            'categories': _('Категория'),
            'content': _('Объявление'),
            'image': _('Изображение')
        }


