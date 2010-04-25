from django.contrib.syndication.views import Feed, FeedDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, get_list_or_404

from models import Category, Entry

class LatestEntries(Feed):

    def get_object(self, request):
        return get_list_or_404(Entry, draft=False)

    def items(self, obj):
        return obj[:30]

    def title(self, obj):
        return "All Posts"

    def link(self, obj):
        return reverse('blog-full-rss')

    def description(self, obj):
        return "All posts on the blog"

    def item_description(self, item):
        return item.body


class LatestEntriesByCategory(Feed):
    
    def get_object(self, request, category):
        return get_object_or_404(Category, name=category)

    def items(self, obj):
        return Entry.objects.filter(categories=obj, draft=False)[:30]

    def title(self, obj):
        return "Posts in the %s category." % obj.name

    def link(self, obj):
        return obj.get_absolute_url()

    def description(self, obj):
        return "Recent posts that were marked %s." % obj.name

    def item_description(self, item):
        return item.body
