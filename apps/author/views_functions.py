from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AuthorForm
from .models import Author

def home(request):
    return render(request, "index.html")
    
def createAuthor(request):
    if(request.method == 'POST'):
        author_form = AuthorForm(request.POST)
        if(author_form.is_valid()):
            author_form.save() 
            return redirect('libro:list_author')
    else: 
        author_form = AuthorForm()
    return render(request, 'libro/create_author.html', {'author_form': author_form})

def listAuthor(request):
    authors = Author.objects.filter(state = True)
    return render(request, 'libro/list_author.html', {'authors': authors})


def editAuthor(request, id):
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
    
    return render(request, 'libro/create_author.html', {'author_form': author_form, 'error': error})
    
def deleteAuthor(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        author.state = False
        author.save()
        return redirect('libro:list_author')
    return render(request, 'libro/delete_author.html', {'author': author})