from django.contrib import admin
from .models import Articles


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titles', 'slug', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('titles', 'descriptions')
    prepopulated_fields = {'slug':('titles',)}
    ordering = ['-status', '-publish']


# Register your models here.
admin.site.register(Articles, ArticleAdmin)
