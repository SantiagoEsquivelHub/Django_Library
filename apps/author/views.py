from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here.
""" 
    View: 
    1. dispatch = validate the request and choose the http method for the request
    2. http_method_not_allowed = returns an error when using undefined http method
    3. options()
"""


class ListAuthor(View):
    """ 
    Contains the logic to list authors

    :param model: Model to use in the class
    :type model: Model
    :param form_class: Django's Form relating to model
    :type model: DjangoForm
    :param template_name: Template to use in the class
    :type template_name: str 

    """

    model = Author
    form_class = AuthorForm
    template_name = 'author/list_author.html'
    context_object_name = 'authors'

    def get_queryset(self):
        """
        Returns the query to use in this class

        :return: a query
        :rtype: queryset

        """
        
        return self.model.objects.filter(state=True)

    def get_context_data(self, **kwargs):
        """
        Returns a context to send to its template

        :return: a context
        :rtype: dist

        """

        context = {}
        context["authors"] = self.get_queryset()
        context["form"] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        """
        Renders a template with a given context 

        :return: render
        :rtype: func

        """
        
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        """
        Redirect to a template, if the given form is valid

        :return: redirect
        :rtype: func

        """
        
        form = self.form_class(request.POST)

        if form.is_valid:
            form.save()
            return redirect('author:list_book')


class CreateAuthor(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/create_author.html'
    success_url = reverse_lazy('author:list_author')

    """ 
    Contains the logic to CREATE an author
    
    :param model: Model to use in the class
    :type model: Model
    :param form_class: Django's Form relating to model
    :type model: DjangoForm
    :param template_name: Template to use in the class
    :type template_name: str 
    :param success_url: URL to render if an author was created successfully
    :type success_url: func
    
    """


class EditAuthor(UpdateView):
    model = Author
    template_name = 'author/edit_author.html'
    form_class = AuthorForm
    success_url = reverse_lazy('author:list_author')

    """ 
    Contains the logic to EDIT an author
    
    :param model: Model to use in the class
    :type model: Model
    :param form_class: Django's Form relating to model
    :type model: DjangoForm
    :param template_name: Template to use in the class
    :type template_name: str 
    :param success_url: URL to render if an author was edited successfully
    :type success_url: func
    
    """


class DeleteAuthor(DeleteView):
    model = Author

    """ 
    Contains the logic to DELETE an author
    
    :param model: Model to use in the class
    :type model: Model
  
    """

    def post(self, request, pk, *args, **kwargs):
        """ 
        DELETE LOGICALLY an author

        :param request: request sent from browser
        :type request: request
        :param pk: Author's primary key
        :type pk: int
        :return: redirect
        :rtype: func

        """

        author = Author.objects.get(id=pk)
        author.state = False
        author.save()
        return redirect('author:list_author')
    
class ListBook(View):
    """ 
    Contains the logic to list books

    :param model: Model to use in the class
    :type model: Model
    :param form_class: Django's Form relating to model
    :type model: DjangoForm
    :param template_name: Template to use in the class
    :type template_name: str 

    """
    
    model = Book
    form_class = BookForm
    template_name = 'book/list_book.html'

    def get_queryset(self):
        """
        Returns the query to use in this class

        :return: a query
        :rtype: queryset

        """
        
        return self.model.objects.filter(state=True)

    def get_context_data(self, **kwargs):
        """
        Returns a context to send to its template

        :return: a context
        :rtype: dist

        """
        
        context = {}
        context["books"] = self.get_queryset()
        context["form"] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        """
        Renders a template with a given context 

        :return: render
        :rtype: func

        """
        
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        """
        Redirect to a template, if the given form is valid

        :return: redirect
        :rtype: func

        """
        
        form = self.form_class(request.POST)

        if form.is_valid:
            form.save()
            return redirect('author:list_book')


class CreateBook(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/create_book.html'
    success_url = reverse_lazy('author:list_book')
    
    """ 
    Contains the logic to CREATE a book
    
    :param model: Model to use in the class
    :type model: Model
    :param form_class: Django's Form relating to model
    :type model: DjangoForm
    :param template_name: Template to use in the class
    :type template_name: str 
    :param success_url: URL to render if a book was edited successfully
    :type success_url: func
    
    """


class EditBook(UpdateView):
    model = Book
    template_name = 'book/edit_book.html'
    form_class = BookForm
    success_url = reverse_lazy('author:list_book')

    """ 
    Contains the logic to EDIT a book
    
    :param model: Model to use in the class
    :type model: Model
    :param form_class: Django's Form relating to model
    :type model: DjangoForm
    :param template_name: Template to use in the class
    :type template_name: str 
    :param success_url: URL to render if a book was edited successfully
    :type success_url: func
    
    """


class DeleteBook(DeleteView):
    model = Book
    template_name = 'book/book_confirm_delete.html'
    """ 
    Contains the logic to DELETE LOGICALLY a book
    
    :param model: Model to use in the class
    :type model: Model
    :param template_name: Template to use in the class
    :type template_name: str
    
    """

    def post(self, request, pk, *args, **kwargs):
        """ 
        DELETE LOGICALLY a book

        :param request: request sent from browser
        :type request: request
        :param pk: Author's primary key
        :type pk: int
        :return: redirect
        :rtype: func

        """
        
        book = Book.objects.get(id=pk)
        book.state = False
        book.save()
        return redirect('author:list_book')
    
class ListAvailableBook(ListView):
    model = Book
    paginate_by = 6
    template_name = 'book/available_book.html'
    
    def get_queryset(self):
        queryset = self.model.objects.filter(state = True, stock__gte = 1)
        return queryset
    
class ListReservation(ListView):
    model = Reservation
    paginate_by = 6
    template_name = 'book/reserved_book.html'
    
    def get_queryset(self):
        queryset = self.model.objects.filter(state = True, user = self.request.user)
        return queryset
    
class DetailBook(DetailView):
    model = Book
    template_name = 'book/detail_book.html'
    
    def get(self, request, *args, **kwargs):
        if self.get_object().stock > 0:
            return render(request, self.template_name, {'object': self.get_object()})
        return redirect('author:list_available_books')
    
class RegisterReservation(CreateView):
    model = Reservation
    success_url = reverse_lazy('author:list_available_books')
    
    def post(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            book = Book.objects.filter(id = request.POST.get('book')).first()
            user = User.objects.filter(id = request.POST.get('user')).first()
            
            if book and user and book.stock > 0:
                new_reservation = self.model(
                    book = book,
                    user = user,
                )
                new_reservation.save()
                message = f'{self.model.__name__} registered successfully'
                error = "There's not error!"
                response = JsonResponse({'message': message, 'error': error, 'url': self.success_url})
                response.status_code = 201
                print(response)
                return response
        return redirect('author:list_available_books')