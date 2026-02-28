from rest_framework.routers import DefaultRouter
from .views import IssueRecordViewSet

router = DefaultRouter()
router.register(r'', IssueRecordViewSet)

urlpatterns = router.urls