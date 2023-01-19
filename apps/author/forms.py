from django import forms
from django.core.exceptions import ValidationError
from .models import *

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'last_name', 'nacionality']
        
        # Modify the attributes' labels
        labels = {
             'name': "Author's name",
             'last_name': "Author's last_name",
             'nacionality': "Author's nacionality",
         }
        #  Modify the attributes' style
        widgets = {
             'name': forms.TextInput(
                 attrs= {
                     'class': 'form-control',
                     'placeholder': "Enter the name of the author",
                 }
                 ),
             'last_name': forms.TextInput(
                 attrs= {
                     'class': 'form-control',
                     'placeholder': "Enter the last name of the author",
                 }
                 ),
             'nacionality': forms.TextInput(
                 attrs= {
                     'class': 'form-control',
                     'placeholder': "Enter the nacionality of the author",
                 }
                 )
         }
         
class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Reservation
        fields = '__all__'
    
    def clean_book(self):
        book = self.cleaned_data['book']
        if book.stock < 1:
            raise ValidationError('This book can not be reserved, there must be units available.')
        return book

class BookForm(forms.ModelForm):
    
     def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.fields['author_id'].queryset = Author.objects.filter(state = True)
     

     class Meta:
         model = Book
         fields = ('title','author_id','publication_date', 'state', 'description', 'image', 'stock')
         labels = {
             'title': "Book's title",
             'author_id': "Book's Authors",
             'publication_date': "Book's Publication Date"
         }
         widgets = {
             'title': forms.TextInput(
                 attrs = {
                     'class': 'form-control',
                     'placeholder': 'Enter the title of book'
                 }
             ),
             'author_id': forms.SelectMultiple(
                 attrs = {
                     'class':'form-control'
                 }
             ),
             'publication_date': forms.SelectDateWidget(
                 attrs = {
                     'class': 'form-control'
                 }
             )
         }