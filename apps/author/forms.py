from django import forms
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
                     'id': 'name'
                 }
                 ),
             'last_name': forms.TextInput(
                 attrs= {
                     'class': 'form-control',
                     'placeholder': "Enter the last name of the author",
                     'id': 'last_name'
                 }
                 ),
             'nacionality': forms.TextInput(
                 attrs= {
                     'class': 'form-control',
                     'placeholder': "Enter the nacionality of the author",
                     'id': 'nacionality'
                 }
                 )
         }
         
# class ReservationForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         #self.fields['libro'].queryset = Libro.objects.filter(estado = True,cantidad__gte = 1)

#     class Meta:
#         model = Reservation
#         fields = '__all__'
    
#     def clean_libro(self):
#         libro = self.cleaned_data['book']
#         if libro.cantidad < 1:
#             raise ValidationError('No se puede reservar este libro, deben existir unidades disponibles.')

#         return libro

class BookForm(forms.ModelForm):
    
     """ def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.fields['author_id'].queryset = Author.objects.filter(state = True) """
    

     class Meta:
         model = Book
         fields = ('title','author_id','publication_date', 'state')
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