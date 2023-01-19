from django.urls import reverse_lazy
from django.forms import formset_factory
from django.views.generic.edit import FormView
from .models import *
from .forms import *

class FormsetAuthor(FormView):
    template_name = 'author/formset_author.html'
    form_class = formset_factory(AuthorForm, extra = 1)
    success_url = reverse_lazy('author:list_author')
    
    def form_valid(self, form):
        for form_unit in form:
            if form_unit.is_valid():
                form_unit.save()
        return super().form_valid(form)