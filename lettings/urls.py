from django.urls import path
from oc_lettings_site import views

urlpatterns = [
    path('', views.lettings_index, name='lettings_index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
