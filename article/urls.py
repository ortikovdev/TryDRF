from django.urls import path
from .views import (
    article_list,
    article_detail,
    article_create,
    list_create_view,
    list_view,
    article_update,
    article_delete,
    article_rud_get,
)

app_name = 'article'

urlpatterns = [
    path('list/', article_list, name='list'),
    path('detail/<int:pk>/', article_detail, name='detail'),
    path('create/', article_create, name='create'),
    path('list-create/', list_create_view, name='list-create'),
    path('list-view/', list_view, name='list-view'),
    path('update/<int:pk>/', article_update, name='update'),
    path('delete/<int:pk>/', article_delete, name='delete'),
    path('rud/<int:pk>/', article_rud_get, name='rud'),
]
