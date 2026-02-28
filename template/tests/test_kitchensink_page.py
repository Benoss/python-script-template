{%- if project_type == "django" %}
"""Tests for the kitchensink showcase page."""

from django.test import Client
from django.urls import reverse


def test_kitchensink_page(client: Client) -> None:
    """Load the kitchensink page successfully."""
    response = client.get(reverse("kitchensink:index"))

    assert response.status_code == 200
    assert b"Kitchensink Components" in response.content
{% endif -%}