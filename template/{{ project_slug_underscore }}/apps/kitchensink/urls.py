"""URL configuration for kitchensink."""

from django.urls import path

from .views import KitchensinkView

app_name = "kitchensink"

urlpatterns = [
    path("", KitchensinkView.as_view(), name="index"),
]
