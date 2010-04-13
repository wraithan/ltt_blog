from django.conf.urls.defaults import *
import dselector

from feeds import LatestEntries, LatestEntriesByCategory


parser = dselector.Parser()
url = parser.url

urlpatterns = parser.patterns('yadba.views',
    url(r'', 'blog_index', name='blog-index'),
    url(r'blog/{year:year}/{month:day}/{slug:slug}/', 'blog_entry', name='blog-entry'),
    url(r'blog/rss/', LatestEntries(), name='blog-full-rss'),
    url(r'blog/{category:word}/', 'blog_category', name='blog-category'),
    url(r'blog/{category:word}/rss/', LatestEntriesByCategory(), name='blog-category-rss'),
)
