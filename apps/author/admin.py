from django.contrib import admin
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    actions = ['elimination_authors_with_filter']
    
    def elimination_authors_with_filter(modeladmin, request, queryset):
        queryset = queryset.exclude(name__icontains = "Diego")
        
        for author in queryset:
            author.delete()
            
    def get_actions(self, request):
        actions = super().get_actions(request)
        
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions    
    
# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)

