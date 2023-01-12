from django.db import models

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
    author_id = models.ManyToManyField(Author)
    state = models.BooleanField('state', default=True)
    creation_date = models.DateField('Creation date', auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name= 'Book'
        verbose_name_plural= 'Books'
        ordering= ['title']
        
    def __str__(self):
        return self.title
    
# class Reservation(models.Model):
#     """Model definition for Reserva."""

#     # TODO: Define fields here
#     id = models.AutoField(primary_key = True)
#     libro = models.ForeignKey(Book, on_delete=models.CASCADE)
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     cantidad_dias = models.SmallIntegerField('Cantidad de Dias a Reservar',default = 7)    
#     fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
#     fecha_vencimiento = models.DateField('Fecha de vencimiento de la reserva', auto_now=False, auto_now_add=False, null = True, blank = True)
#     estado = models.BooleanField(default = True, verbose_name = 'Estado')

#     class Meta:
#         """Meta definition for Reserva."""

#         verbose_name = 'Reserva'
#         verbose_name_plural = 'Reservas'

#     def __str__(self):
#         """Unicode representation of Reserva."""
#         return f'Reserva de Libro {self.libro} por {self.usuario}'