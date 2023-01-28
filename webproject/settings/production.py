from .common import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['52.62.10.15', '127.0.0.1', 'localhost ', '*']
# HAYSTACK_CONNECTIONS['default']['URL'] = 'http://hellodjango_blog_tutorial_elasticsearch:9200/'
