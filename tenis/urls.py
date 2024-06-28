from django.urls import include, path
from rest_framework import routers
from .views import BrandViewSet, ShoeViewSet

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'shoes', ShoeViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
]