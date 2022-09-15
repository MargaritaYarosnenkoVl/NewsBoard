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


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostCategory)
admin.site.register(UserCategory)
