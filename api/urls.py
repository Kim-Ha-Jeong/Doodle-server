from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'photo', PhotoViewSet)
router.register(r'review', ReviewViewSet)
urlpatterns = router.urls
