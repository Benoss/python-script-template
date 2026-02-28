"""Render the kitchensink component showcase."""

from django.views.generic import TemplateView


class KitchensinkView(TemplateView):
    """Render the kitchensink component gallery page."""

    template_name = "kitchensink/index.html"
