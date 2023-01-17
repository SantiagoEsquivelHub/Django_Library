from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('home_user', HomeUser.as_view(), name='home_user'),
    path('list_user', ListUser.as_view(), name='list_user'),
    path('create_user', RegisterUser.as_view(), name='create_user'),
    path('edit_user/<int:pk>/', EditUser.as_view(), name='edit_user'),
    path('delete_user/<int:pk>/', DeleteUser.as_view(), name='delete_user'),
]


