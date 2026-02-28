from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookCopyViewSet

router = DefaultRouter()
router.register(r'', BookViewSet)
router.register(r'copies', BookCopyViewSet)

urlpatterns = router.urls