from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    subscribers = models.ManyToManyField(User, through='UserCategory')

    def __str__(self):
        return self.name

    def get_subscribers_emails(self):
        result = set()
        for user in self.subscribers.all():
            result.add(user.email)
        return result


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    image = models.ImageField()
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')


    categories = models.ManyToManyField(Category, through='PostCategory', verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=255,  verbose_name='Текст')

    comment_data = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False, verbose_name='Принято')

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f'{self.text}'

    def is_accept(self):
        return self.accepted

    '''class Meta:
        ordering = ('comment_data',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.post)'''


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class UserCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
