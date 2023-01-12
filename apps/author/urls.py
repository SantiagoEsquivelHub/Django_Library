from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns = [
   path('create_author/', login_required(CreateAuthor.as_view()), name='create_author'),
   path('list_author/', login_required(ListAuthor.as_view()), name='list_author'),
   path('edit_author/<int:pk>', login_required(EditAuthor.as_view()), name='edit_author'),
   path('delete_author/<int:pk>', login_required(DeleteAuthor.as_view()), name='delete_author'),
]
