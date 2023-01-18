from django.contrib import admin
from .forms import *
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ReservationAdmin(admin.ModelAdmin):
    form = ReservationForm
    list_display = ['book', 'user', 'creation_date', 'state']

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class AuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    search_fields = ['name', 'last_name', 'nacionality']
    list_display = ['name', 'last_name', 'nacionality', 'state']
    resource_class = AuthorResource
    actions = ['logic_elimination_authors', 'elimination_authors_with_filter']
    
    def elimination_authors_with_filter(modeladmin, request, queryset):
        queryset = queryset.exclude(name__icontains = "Diego")
        
        for author in queryset:
            author.delete()
    
    def logic_elimination_authors(modeladmin, request, queryset):
        for author in queryset:
            author.state = False
            author.save()
            
    def logic_activation_authors(modeladmin, request, queryset):
        for author in queryset:
            author.state = True
            author.save()
            
    def get_actions(self, request):
        actions = super().get_actions(request)
        
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions    
    

    
    
# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
admin.site.register(Reservation, ReservationAdmin)

