from django.db import models
from django.db.models.signals import post_save, pre_save
from apps.user.models import *
# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=220, blank=False, null=False)
    nacionality = models.CharField(max_length=100, blank=False, null=False)
    state = models.BooleanField('state', default=True)
    creation_date = models.DateField('Creation date', auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name= 'Author'
        verbose_name_plural= 'Authors'
        ordering= ['name']
        
    def __str__(self):
        return self.name
    
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('title', max_length=255, blank=False, null=False)
    publication_date = models.DateField('Publication date', blank=False, null=False)
    description = models.CharField('Description', max_length=255, blank=True, null=True)
    stock = models.SmallIntegerField('Stock', default=1)
    image = models.ImageField('Image', upload_to='books/', max_length=225, blank=True, null=True)
    author_id = models.ManyToManyField(Author)
    state = models.BooleanField('state', default=True)
    creation_date = models.DateField('Creation date', auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name= 'Book'
        verbose_name_plural= 'Books'
        ordering= ['title']
        
    def __str__(self):
        return self.title
    
    def get_authors(self):
        authors = str([author for author in self.author_id.all().values_list('name', flat = True)]).replace("[", "").replace("]", "").replace("'", "")
        return authors
    
def remove_relationship_author_book(sender, instance, **kwargs):
    if instance.state == False:
        author_id = instance.id
        books = Book.objects.filter(author_id = author_id)
        
        for book in books:
            book.author_id.remove(author_id)
        
def reduce_stock(sender, instance, **kwargs):
    book = instance.book
    if book.stock > 0:
        book.stock -= 1
        book.save() 


        
class Reservation(models.Model):
    """Model definition for Reservation."""

    # TODO: Define fields here
    id = models.AutoField(primary_key = True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_days = models.SmallIntegerField('Number of days to reserve',default = 7)    
    creation_date = models.DateField('Creation date', auto_now = False, auto_now_add = True)
    expiration_date = models.DateField('Reservation expiration date', auto_now=False, auto_now_add=False, null = True, blank = True)
    state = models.BooleanField(default = True, verbose_name = 'State')

    class Meta:
        """Meta definition for Reservation."""

        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        """Unicode representation of Reserva."""
        return f'Book reservation {self.book} by {self.user}'
    
post_save.connect(remove_relationship_author_book, sender = Author)
post_save.connect(reduce_stock, sender = Reservation)
    
