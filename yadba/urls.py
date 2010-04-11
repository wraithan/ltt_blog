from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse
import dselector

from feeds import LatestEntries, LatestEntriesByCategory


parser = dselector.Parser()
url = parser.url

urlpatterns = parser.patterns('yadba.views',
    url(r'', 'blog_index', name='blog-index'),
    url(r'blog/{year:year}/{month:day}/{slug:slug}/', 'blog_view_entry', name='blog-view-entry'),
    url(r'blog/rss/', LatestEntries(), name='blog-full-feed'),
    url(r'blog/{category:word}/rss/', LatestEntriesByCategory(), name='blog-category-rss'),
)
