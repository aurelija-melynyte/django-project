from django.urls import path
from . import views


urlpatterns = [
    path('quote',  views.QuoteViewSet.as_view()),
]
