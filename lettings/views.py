"""
This module defines the views for the 'lettings' application.

Each function in this module is a separate view that Django can render.
The views receive an HttpRequest object, perform operations based on the request,
and return an HttpResponse object.
"""

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Letting
from logging import getLogger


logger = getLogger(__name__)


def index(request):
    """
    Display a list of all lettings.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object, which includes a context containing a list
         of all lettings.
    """
    logger.info(
        "Client with IP %s accessed the lettings index page",
        request.META.get("REMOTE_ADDR"),
    )
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Display a specific letting.

    Args:
        request (HttpRequest): The request object.
        letting_id (int): The ID of the letting to display.

    Returns:
        HttpResponse: The response object, which includes a context containing the
         letting's title and address.

    Raises:
        Http404: If no Letting exists with the given ID.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        logger.info(
            "Client with IP %s accessed the letting %s page",
            request.META.get("REMOTE_ADDR"),
            letting_id,
        )

    except Http404:
        logger.warning(
            "Client with IP %s tried to access a letting that does not exist: %s",
            request.META.get("REMOTE_ADDR"),
            letting_id,
        )
        raise

    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
