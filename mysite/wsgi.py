"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# application = get_wsgi_application()

import os
import sys
# from whitenoise import WhiteNoise
path = '/home/mariachern3/django'  # use your own username here
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise
# application = DjangoWhiteNoise(get_wsgi_application())

from whitenoise import WhiteNoise
application = WhiteNoise(get_wsgi_application())