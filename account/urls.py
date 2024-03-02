from django.urls import path
from rest_framework.authtoken import views as auth_view
from .views import logout_view

app_name = 'account'


urlpatterns = [
    path('login/', auth_view.obtain_auth_token, name='login'),
    path('logout/', logout_view, name='logout'),
]