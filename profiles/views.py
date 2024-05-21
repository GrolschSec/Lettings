"""
This module defines the views for the 'profiles' application.

Each function in this module is a separate view that Django can render.
The views receive an HttpRequest object, perform operations based on the request,
and return an HttpResponse object.
"""

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Profile
from logging import getLogger


logger = getLogger(__name__)


def index(request):
    """
    Display a list of all profiles.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    logger.info(
        "Client with IP %s accessed the profiles index page",
        request.META.get("REMOTE_ADDR"),
    )
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Display a specific profile.

    Args:
        request (HttpRequest): The request object.
        username (str): The username of the profile to display.

    Returns:
        HttpResponse: The response object.

    Raises:
        Http404: If no Profile exists with the given username.
    """

    try:
        profile = get_object_or_404(Profile, user__username=username)
        logger.info(
            "Client with IP %s accessed the profile %s page",
            request.META.get("REMOTE_ADDR"),
            username,
        )

    except Http404:
        logger.warning(
            "Client with IP %s tried to access a profile that does not exist: %s",
            request.META.get("REMOTE_ADDR"),
            username,
        )
        raise

    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
