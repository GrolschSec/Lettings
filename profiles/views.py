"""
This module defines the views for the 'profiles' application.

Each function in this module is a separate view that Django can render.
The views receive an HttpRequest object, perform operations based on the request,
and return an HttpResponse object.
"""

from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):
    """
    Display a list of all profiles.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
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
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
