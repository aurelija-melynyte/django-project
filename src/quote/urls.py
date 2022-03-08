from django.urls import path
from . import views

"""
A URL pattern describes the way the URL is laid out. It also tells Django what to look for when matching
a browser request with a site URL so it knows which page to return. Each URL then maps to a particular
view and the view function retrieves and processes the data needed for that page.
"""

urlpatterns = [
    path('quote',  views.QuoteViewSet.as_view()),
]
