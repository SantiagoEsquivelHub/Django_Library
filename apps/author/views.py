from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AuthorForm
from .models import Author
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

""" def home(request):
    return render(request, "index.html") """
    
""" def createAuthor(request):
    if(request.method == 'POST'):
        author_form = AuthorForm(request.POST)
        if(author_form.is_valid()):
            author_form.save() 
            return redirect('libro:list_author')
    else: 
        author_form = AuthorForm()
    return render(request, 'libro/create_author.html', {'author_form': author_form}) """

""" def listAuthor(request):
    authors = Author.objects.filter(state = True)
    return render(request, 'libro/list_author.html', {'authors': authors}) """
    
""" 
    View: 
    1. dispatch = validate the request and choose the http method for the request
    2. http_method_not_allowed = returns an error when using undefined http method
    3. options()
"""

""" def editAuthor(request, id):
    author_form = None
    try:
        author = Author.objects.get(id=id)
        error = None
        
        if request.method == 'GET':
            author_form = AuthorForm(instance=author)
        else: 
            author_form = AuthorForm(request.POST, instance=author)
        
            if(author_form.is_valid()):
                author_form.save() 
    
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request, 'libro/create_author.html', {'author_form': author_form, 'error': error}) """
    
""" def deleteAuthor(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        author.state = False
        author.save()
        return redirect('libro:list_author')
    return render(request, 'libro/delete_author.html', {'author': author}) """
    
# @login_required
class Home(TemplateView):
    template_name = 'index.html'

class CreateAuthor(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/create_author.html'
    success_url = reverse_lazy('author:list_author')


class ListAuthor(ListView):
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

    
