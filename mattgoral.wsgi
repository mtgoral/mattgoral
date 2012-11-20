import os
import sys
sys.path.append('/home/ubuntu/')
sys.path.append('/home/ubuntu/mattgoral/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mattgoral.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()