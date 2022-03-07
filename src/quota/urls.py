from django.urls import path, include

from . import views


urlpatterns = [
    path('quota',  views.QuotaViewSet.as_view()),
]
