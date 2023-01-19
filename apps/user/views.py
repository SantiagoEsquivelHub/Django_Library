import json
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import login 
from django.core.serializers import serialize
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import *
from .models import *
from .mixins import *

class Home(LoginRequiredMixin, TemplateView):
    # Class that renders system index
    template_name = 'index.html'


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)
    
class HomeUser(LoginAndStaffMixin, ValidateRequiredUsersPermissionsMixin, TemplateView):
    template_name = "user/list_user.html"

class ListUser(LoginAndStaffMixin, ValidateRequiredUsersPermissionsMixin, ListView):
    model = User
    template_name = 'user/list_user.html'
    context_object_name = 'users'

    def get_queryset(self):
        dir = ''
        if self.request.GET.get('dir') == 'asc': dir = '' 
        else: dir = '-' 
              
        return self.model.objects.filter(is_active=True, 
                                         name__contains = self.request.GET.get('filter'),
                                         last_name__contains = self.request.GET.get('filter'),
                                         email__contains = self.request.GET.get('filter'),
                                         ).values('id', 'username', 'name', 'last_name', 'email'
                                                  ).order_by(dir + self.request.GET.get('order_by'))

    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            start = int(request.GET.get('start'))
            limit = int(request.GET.get('limit'))
            data_users = self.get_queryset()
            list_users = []
            for index, value in enumerate(data_users[start:start+limit], start):
                list_users.append(value)
                
            data = {
                'length': data_users.count(),
                'objects': list_users
            }
            # data = serialize("json", self.get_queryset())
            return HttpResponse(json.dumps(data), "application/json")
        else:
            return redirect("user:list_user")


class RegisterUser(LoginAndStaffMixin, ValidateRequiredUsersPermissionsMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/create_user.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                new_user = User(
                    email=form.cleaned_data.get('email'),
                    username=form.cleaned_data.get('username'),
                    name=form.cleaned_data.get('name'),
                    last_name=form.cleaned_data.get('last_name'),
                )
                new_user.set_password(form.cleaned_data.get('password1'))
                new_user.save()
                message = f"{self.model.__name__} created successfully" 
                error = "There's not error!"
                response = JsonResponse({"message": message, "error": error})
                response.status_code = 201 # Created
                return response
            else:
                message = f"{self.model.__name__} can not be created" 
                error = form.errors
                response = JsonResponse({"message": message, "error": error})
                response.status_code = 400 # Bad request
                return response
        else:
            return redirect("user:home_user")

class EditUser(LoginAndStaffMixin, ValidateRequiredUsersPermissionsMixin, UpdateView):
    model = User
    form_class = EditUserForm
    template_name = "user/edit_user.html"
    
    def post(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                message = f"{self.model.__name__} edited successfully" 
                error = "There's not error!"
                response = JsonResponse({"message": message, "error": error})
                response.status_code = 200 # OK
                return response
            else:
                message = f"{self.model.__name__} can not be edited" 
                error = form.errors
                response = JsonResponse({"message": message, "error": error})
                response.status_code = 400 # Bad request
                return response
        else:
            return redirect("user:home_user")
        
class DeleteUser(LoginAndStaffMixin, ValidateRequiredUsersPermissionsMixin, DeleteView):
    model = User
    template_name = "user/delete_user.html"

    def post(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            user = self.get_object()
            user.is_active = False
            user.save()
            message = f"{self.model.__name__} deleted successfully" 
            error = "There's not error!"
            response = JsonResponse({"message": message, "error": error})
            response.status_code = 200 # OK
            return response
        else:
            return redirect("user:home_user")
        
        