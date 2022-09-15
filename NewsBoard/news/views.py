from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
#from .filters import SearchFilter
from .models import Post, Category
from django.db.models import Q
from .forms import PostForm


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


class NewsDelete(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = ''


class NewsUpgrade(PermissionRequiredMixin, UpdateView):
    template_name = 'add.html'
    form_class = PostForm
    permission_required = ('news.change_post')


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)