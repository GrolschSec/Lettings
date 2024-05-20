"""
This module defines the views for the 'lettings' application.

Each function in this module is a separate view that Django can render. 
The views receive an HttpRequest object, perform operations based on the request, 
and return an HttpResponse object.
"""

from django.shortcuts import render, get_object_or_404
from .models import Letting


def index(request):
    """
    Display a list of all lettings.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object, which includes a context containing a list of all lettings.
    """
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
        HttpResponse: The response object, which includes a context containing the letting's title and address.

    Raises:
        Http404: If no Letting exists with the given ID.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
