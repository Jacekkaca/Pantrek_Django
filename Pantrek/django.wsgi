import os
import sys

paths = [ '/var/www/html/Pantrek',
          '/var/www/html/Pantrek/Pantrek_app',
          '/usr/lib/python2.7/dist-packages',
]

for path in paths:
    if path not in sys.path:
        sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Pantrek.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


