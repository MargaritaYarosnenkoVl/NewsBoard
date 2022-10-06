from django import forms
from django.forms import ModelForm, CharField, HiddenInput
from django.utils.translation import gettext_lazy as _
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'categories', 'user']
        widgets = {
            'user': forms.HiddenInput(),
        }
        labels = {
            'title': _('Заголовок'),
            'categories': _('Категория'),
            'content': _('Объявление'),
            'image': _('Изображение')
        }


class CommentForm(forms.ModelForm):
    #text = forms.CharField(label='Текст', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }

    '''def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'''


