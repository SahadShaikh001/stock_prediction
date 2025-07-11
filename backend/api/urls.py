from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register),
    path("predict/", views.predict),
    path("predictions/", views.predictions),
]
