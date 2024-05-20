"""
This module configures the ASGI application for Django.

ASGI (Asynchronous Server Gateway Interface) is the standard for Python asynchronous web apps and servers.
This module sets the DJANGO_SETTINGS_MODULE environment variable to point to the Django project's settings and then gets the ASGI application instance.

The application instance is used by the ASGI server to interact with the Django project.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

application = get_asgi_application()
