from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title_text','content_path']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),    
    ]
    list_display = ('title_text', 'content_path', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title_text']
admin.site.register(Article, ArticleAdmin)