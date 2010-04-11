from django.contrib.syndication.views import Feed, FeedDoesNotExist
from django.shortcuts import get_object_or_404

from models import Category, Entry

class LatestEntriesByCategory(Feed):
    
    def get_object(self, request, category):
        return get_object_or_404(Category, name=category)

    def items(self, obj):
        return Entry.objects.filter(categories=obj)[:30]

    def title(self, obj):
        return "Posts in the %s category." % obj.name

    def link(self, obj):
        return obj.get_absolute_url()

    def description(self, obj):
        return "Recent posts that were marked %s." % obj.name

    def item_description(self, item):
        return item.body
