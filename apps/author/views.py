from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
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

class ListBook(View):
    model = Book
    form_class = BookForm
    template_name = 'book/list_book.html'

    def get_queryset(self):
        return self.model.objects.filter(state = True)
    
    def get_context_data(self, **kwargs):
        context = {}
        context["books"] = self.get_queryset() 
        context["form"] = self.form_class
        return context
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid:
            form.save()
            return redirect('author:list_book')
    
class CreateBook(CreateView): 
    model = Book
    form_class = BookForm
    template_name = 'book/create_book.html'
    success_url = reverse_lazy('author:list_book')

class EditBook(UpdateView):
    model = Book
    template_name = 'book/edit_book.html'
    form_class = BookForm
    success_url = reverse_lazy('author:list_book')
    
    """ def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context """
    
class DeleteBook(DeleteView):
    model = Book
    template_name = 'book/book_confirm_delete.html'
    
    def post(self, request, pk, *args, **kwargs):
        book = Book.objects.get(id=pk)
        book.state = False
        book.save()
        return redirect('author:list_book')