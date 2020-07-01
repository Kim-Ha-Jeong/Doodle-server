from rest_framework import routers
from api.views import *
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'review', ReviewViewSet)
urlpatterns = router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#if settings.DEBUG: