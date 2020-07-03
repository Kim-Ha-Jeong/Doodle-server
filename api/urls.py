from rest_framework import routers
from api.views import *
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'review', ReviewViewSet)
router.register(r'produce', ReviewViewSet)

urlpatterns = router.urls
