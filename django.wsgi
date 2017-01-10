import os
import sys
sys.path.append('/home/un/Project/legend')
os.environ['DJANGO_SETTINGS_MODULE'] = 'legend.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

