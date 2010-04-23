from django.contrib import admin

from models import Category, Entry


class EntryAdmin(admin.ModelAdmin):
    fields = ('title', 'body', 'draft', 'tags', 'categories')


admin.site.register(Category)
admin.site.register(Entry, EntryAdmin) 

