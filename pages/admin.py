from django.contrib import admin

from models import Page

class SectionAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display    = ('id', 'url', 'page_title', 'main_article', 'sidebar')
    list_editable   = ('page_title', 'main_article', 'main_article', 'sidebar')
    ordering        = ('page_title',)
    search_fields   = ('page_title', 'main_article', 'sidebar')

admin.site.register(Page, SectionAdmin)
