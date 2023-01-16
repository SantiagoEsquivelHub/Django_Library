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
from .forms import *
from .models import *

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

class ListUser(ListView):
    model = User
    template_name = 'user/list_user.html'
    context_object_name = 'users'

    def get_queryset(self):
        return self.model.objects.filter(active_user=True)

    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = serialize("json", self.get_queryset())
            return HttpResponse(data, "application/json")
        else:
            return redirect("user:list_user")


class RegisterUser(CreateView):
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

class EditUser(UpdateView):
    model = User
    form_class = UserForm
    template_name = "user/edit_user.html"
    
    def post(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                message = f"{self.model.__name__} edited successfully" 
                error = "There's not error!"
                response = JsonResponse({"message": message, "error": error})
                response.status_code = 201 # Created
                return response
            else:
                message = f"{self.model.__name__} can not be edited" 
                error = form.errors
                response = JsonResponse({"message": message, "error": error})
                response.status_code = 400 # Bad request
                return response
        else:
            return redirect("user:home_user")