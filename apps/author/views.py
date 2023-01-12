from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import *
from .models import *

# Create your views here.
""" 
    View: 
    1. dispatch = validate the request and choose the http method for the request
    2. http_method_not_allowed = returns an error when using undefined http method
    3. options()
"""

class Home(TemplateView):
    template_name = 'index.html'

class CreateAuthor(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/create_author.html'
    success_url = reverse_lazy('author:list_author')


class ListAuthor(ListView):
    model = Author
    template_name = 'author/list_author.html'
    queryset = Author.objects.filter(state = True)
    context_object_name = 'authors'
        

class EditAuthor(UpdateView):
    model = Author
    template_name = 'author/create_author.html'
    form_class = AuthorForm
    success_url = reverse_lazy('author:list_author')
    
        
    
class DeleteAuthor(DeleteView):
    model = Author
    # success_url = reverse_lazy('author:list_author')

    """ Logic deleting """
    def post(self, request, pk, *args, **kwargs):
        author = Author.objects.get(id=pk)
        author.state = False
        author.save()
        return redirect('author:list_author')

class ListBook(ListView):
    model = Book
    template_name = 'book/list_book.html'
    queryset = Book.objects.filter(state = True)
    context_object_name = 'books'
    
class CreateBook(CreateView): 
    model = Book
    form_class = BookForm
    template_name = 'book/create_book.html'
    success_url = reverse_lazy('author:list_book')

class EditBook(UpdateView):
    model = Book
    template_name = 'book/create_book.html'
    form_class = BookForm
    success_url = reverse_lazy('author:list_book')
    
class DeleteBook(DeleteView):
    model = Book
    template_name = 'book/book_confirm_delete.html'
    
    def post(self, request, pk, *args, **kwargs):
        book = Book.objects.get(id=pk)
        book.state = False
        book.save()
        return redirect('author:list_book')