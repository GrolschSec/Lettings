"""
This module configures and creates a WSGI application for the 'oc_lettings_site' Django project.

WSGI (Web Server Gateway Interface) is a standard interface between web servers
 and web applications.
This module sets the DJANGO_SETTINGS_MODULE environment variable to point to
 the Django project's settings
and then creates a WSGI application using Django's get_wsgi_application function.

This WSGI application can be served using various WSGI servers such as Gunicorn or uWSGI.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

application = get_wsgi_application()
