import os, sys
sys.path.append('/srv/wsgi')
sys.path.append('/srv/wsgi/ltt_blog')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ltt_blog.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
