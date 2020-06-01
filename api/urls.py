from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'test', TestViewSet)
router.register(r'test2', Test2ViewSet)
urlpatterns = router.urls
