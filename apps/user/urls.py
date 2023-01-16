from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('list_user', login_required(ListUser.as_view()), name='list_user'),
    path('create_user', login_required(RegisterUser.as_view()), name='create_user'),
    path('edit_user/<int:pk>/', login_required(EditUser.as_view()), name='edit_user'),
    
]

urlpatterns += [
    path('home_user', login_required(
        TemplateView.as_view(
            template_name="user/list_user.html"
        )
    ), name='home_user'),
]
