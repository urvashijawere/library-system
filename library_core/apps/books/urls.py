from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookCopyViewSet, AddBookCopiesAPIView
from django.urls import path, include

# router = DefaultRouter()
# router.register(r'', BookViewSet)

urlpatterns = [
    # path('', include(router.urls)),   # ViewSet URLs
    path('copies/', AddBookCopiesAPIView.as_view(), name='book-copies'),  # APIView URL
]