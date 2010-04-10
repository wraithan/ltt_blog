from django.conf.urls.defaults import *
import dselector


parser = dselector.Parser()
url = parser.url

urlpatterns = parser.patterns('yadba.views',
    url(r'!', 'blog_index', name='blog-index'),
)
