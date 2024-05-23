"""
This module defines the views for the 'oc_lettings_site' application.

Each function in this module is a separate view that Django can render.
The views receive an HttpRequest object, perform operations based on the request,
and return an HttpResponse object.
"""

from django.shortcuts import render
from logging import getLogger


logger = getLogger(__name__)


def index(request):
    """
    Display the index page of the 'oc_lettings_site' application.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object, which renders
            the 'oc_lettings_site/index.html' template.
    """
    logger.info(
        "Client with IP %s accessed the index page", request.META.get("REMOTE_ADDR")
    )
    dd = 7 / 0
    return render(request, "oc_lettings_site/index.html")
