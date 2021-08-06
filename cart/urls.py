from django.urls import path, include
from rest_framework.routers import SimpleRouter
from cart.views import CartViewSet

router = SimpleRouter()
router.register('cart', CartViewSet)


urlpatterns = [
    path('', include(router.urls)),
]