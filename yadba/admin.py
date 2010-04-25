from django.contrib import admin

from models import Category, Entry, PoweredBy


class EntryAdmin(admin.ModelAdmin):
    fields = ('title', 'body', 'draft', 'tags', 'categories')


admin.site.register(Category)
admin.site.register(Entry, EntryAdmin) 
admin.site.register(PoweredBy)
