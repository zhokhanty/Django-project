from django.urls import path
from .views import create_news, edit_news, delete_news, news_list

urlpatterns = [
    path('create/', create_news, name='create_news'),
    path('<int:news_id>/edit/', edit_news, name='edit_news'),
    path('', news_list, name='news_list'),
    path('<int:news_id>/delete/', delete_news, name='delete_news'),
]
