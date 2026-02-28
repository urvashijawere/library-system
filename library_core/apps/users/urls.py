from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MemberViewSet

router = DefaultRouter()
router.register("members", MemberViewSet, basename="members")
router.register("", UserViewSet, basename="users")

urlpatterns = router.urls