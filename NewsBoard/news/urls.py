from django.urls import path
from .views import NewsList, NewsDetail, Search, NewsAdd, NewsUpgrade, NewsDelete
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', NewsList.as_view(), name='index'),
    path('<int:pk>', NewsDetail.as_view(), name='news'),
    path('search/', Search.as_view(), name='search_results'),
    path('add/', NewsAdd.as_view(), name='add'),
    path('<int:pk>/edit', NewsUpgrade.as_view(), name='edit'),
    path('<int:pk>/delete', NewsDelete.as_view(), name='delete'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout')
    ]