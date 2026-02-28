"""Configure the Kitchensink app."""

from django.apps import AppConfig


class KitchensinkConfig(AppConfig):
    """Provide app configuration for Kitchensink."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "django_starter.apps.kitchensink"
    verbose_name = "Kitchensink"
