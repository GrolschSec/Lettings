from django.urls import path
from oc_lettings_site import views

urlpatterns = [
    path('', views.profiles_index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]
