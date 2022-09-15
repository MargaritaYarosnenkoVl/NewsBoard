'''from django_filters import FilterSet, CharFilter
from .models import Post


class SearchFilter(FilterSet):
    title = CharFilter(field_name='post__title', label='По заголовку')
    content = CharFilter(field_name='post__content', label='В объявлениях')
    author = CharFilter(field_name='post__author', label='По автору')
    categorys = CharFilter(field_name='post__categorys', label='По категории')

    class Meta:
        model = Post
        fields = {'content', 'title', 'author', 'categorys'}'''