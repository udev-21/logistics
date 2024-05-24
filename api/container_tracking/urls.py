from django.urls import path

from api.container_tracking.views import ContainerTrackingListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"container-tracking", ContainerTrackingListView, basename="user")

urlpatterns = router.urls
