from django.contrib import admin
from .models import Category, Post, PostCategory, Comment, UserCategory
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'comment_data', 'accepted')
    list_filter = ('accepted', 'comment_data')
    search_fields = ('user',  'text')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
