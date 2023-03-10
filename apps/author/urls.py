from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *
from .formsets import *

urlpatterns = [
   path('list_author/', login_required(ListAuthor.as_view()), name='list_author'),
   path('create_author/', login_required(CreateAuthor.as_view()), name='create_author'),
   path('edit_author/<int:pk>', login_required(EditAuthor.as_view()), name='edit_author'),
   path('delete_author/<int:pk>', login_required(DeleteAuthor.as_view()), name='delete_author'),
   path('list_book/', login_required(ListBook.as_view()), name='list_book'),
   path('create_book/', login_required(CreateBook.as_view()), name='create_book'),
   path('edit_book/<int:pk>', login_required(EditBook.as_view()), name='edit_book'),
   path('delete_book/<int:pk>', login_required(DeleteBook.as_view()), name='delete_book'),
   # GENERALS URLS
   path('list-available-books/', login_required(ListAvailableBook.as_view()), name='list_available_books'),
   path('list-reservation-books/', login_required(ListReservation.as_view()), name='list_reservation_books'),
   path('expired-reserved-books/', login_required(ListExpiredReservation.as_view()), name='expired_reserved_books'),
   path('detail-book/<int:pk>/', login_required(DetailBook.as_view()), name='detail_book'),
   path('reserve-book/', login_required(RegisterReservation.as_view()), name='reserve_book'),
   #FORMSETS
   path('create_author_formset/', login_required(FormsetAuthor.as_view()), name='create_author_formset'),
]
