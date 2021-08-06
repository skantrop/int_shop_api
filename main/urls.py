from django.urls import path, include
from rest_framework.routers import SimpleRouter
from main.views import ReviewViewSet, ProductViewSet, FavoriteView
from django.conf import settings
from django.conf.urls.static import static

router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('reviews', ReviewViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/favorites/', FavoriteView.as_view()),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)