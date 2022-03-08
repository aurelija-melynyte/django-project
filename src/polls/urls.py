from django.urls import path, include
from rest_framework import routers

from . import views

# include() - a function that takes a full Python import path to another URLconf module
# that should be “included” in this place.

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'cats', views.CatViewSet)


# automatic URL routing.
# include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]