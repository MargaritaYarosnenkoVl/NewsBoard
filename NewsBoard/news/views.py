import random

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
#from .filters import SearchFilter
from .models import Post, Category, Comment
from django.db.models import Q
from .forms import PostForm, CommentForm


class NewsList(ListView):
    model = Post
    ordering = '-id'
    template_name = 'home.html'
    context_object_name = 'home'
    paginate_by = 6
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['category'] = Category.objects.all()
        context['form'] = PostForm()
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    '''def get(self, request, post, *args, **kwargs):
        post = get_object_or_404(Post, slug=post)
        common_tags = Post.tag.most_common()
        last_posts = Post.objects.all().order_by('-id')[:5]
        comment_form = CommentForm()
        return render(request, 'news.html', context={
            'post': post,
            'common_tags': common_tags,
            'last_posts': last_posts,
            'comment_form': comment_form
        })

    def post(self, request, slug, post, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            post = get_object_or_404(Post, slug=post)
            comment = Comment.objects.create(post=post, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'news.html', context={
            'comment_form': comment_form
        })'''

    '''def post_detail(request, year, month, day, post):
        post = get_object_or_404(Post, slug=post,
                                 status='published',
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day)
        # List of active comments for this post
        comments = post.comments.filter(accepted=True)

        if request.method == 'POST':
            # A comment was posted
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                # Create Comment object but don't save to database yet
                new_comment = comment_form.save(commit=False)
                # Assign the current post to the comment
                new_comment.post = post
                # Save the comment to the database
                new_comment.save()
        else:
            comment_form = CommentForm()
        return render(request,
                      'news.html',
                      {'post': post,
                       'comments': comments,
                       'comment_form': comment_form})'''

class Search(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        results = ""
        if query:
            results = Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        paginator = Paginator(results, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'search.html', context={
            'title': 'Поиск',
            'results': page_obj,
            'count': paginator.count
        })


class NewsAdd(PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'add.html'
    form_class = PostForm
    permission_required = ('news.add_post')

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = self.request.user
        return initial


class NewsDelete(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/'


class NewsUpgrade(PermissionRequiredMixin, UpdateView):
    template_name = 'add.html'
    form_class = PostForm
    permission_required = ('news.change_post')


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)



'''def usual_login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        OneTimeCode.objects.create(code=random.choice('abcde'), user=user)
        if user.is_active:
            login(request, user)
            #send code
            #redirect
        else:
            return HttpResponse('Invalid login')


def login_with_code_view(request):
    username = request.POST['username']
    code = request.POST['code']
    if OneTimeCode.objects.filter(code=code, user__username=username).exits():
        login(request, user)
        else:
            return HttpResponse('Disabled account')'''