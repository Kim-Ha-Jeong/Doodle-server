from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'test', TestViewSet)
urlpatterns = router.urls
