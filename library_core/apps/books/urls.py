from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookCopyViewSet, AddBookCopiesAPIView
from django.urls import path, include

router = DefaultRouter()
router.register(r'book-copies', BookCopyViewSet)
router.register(r'', BookViewSet)

urlpatterns = [
    path('copies/', AddBookCopiesAPIView.as_view(), name='copies'), # APIView URL
    path('', include(router.urls)), # ViewSet URLs
]