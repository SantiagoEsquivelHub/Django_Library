from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns = [
   path('list_author/', login_required(ListAuthor.as_view()), name='list_author'),
   path('create_author/', login_required(CreateAuthor.as_view()), name='create_author'),
   path('edit_author/<int:pk>', login_required(EditAuthor.as_view()), name='edit_author'),
   path('delete_author/<int:pk>', login_required(DeleteAuthor.as_view()), name='delete_author'),
   path('list_book/', login_required(ListBook.as_view()), name='list_book'),
   path('create_book/', login_required(CreateBook.as_view()), name='create_book'),
   path('edit_book/<int:pk>', login_required(EditBook.as_view()), name='edit_book'),
   path('delete_book/<int:pk>', login_required(DeleteBook.as_view()), name='delete_book'),
   
]
