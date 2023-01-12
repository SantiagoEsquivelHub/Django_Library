
class ListBook(ListView):
    model = Book
    template_name = 'book/list_book.html'
    queryset = Book.objects.filter(state = True)
    context_object_name = 'books'
    
class EditBook(UpdateView):
    model = Book
    template_name = 'book/create_book.html'
    form_class = BookForm
    success_url = reverse_lazy('author:list_book')