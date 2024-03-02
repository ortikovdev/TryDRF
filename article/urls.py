from django.urls import path
from .views import (
    article_list,
    article_detail,
    article_create,
    list_create_view,
)

app_name = 'article'

urlpatterns = [
    path('list/', article_list, name='list'),
    path('detail/<int:pk>', article_detail, name='detail'),
    path('create/', article_create, name='create'),
    path('list-create/', list_create_view, name='list-create'),
]