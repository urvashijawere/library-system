from django.db.models import ProtectedError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import MemberProfile, User
from .serializers import MemberProfileSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    queryset = MemberProfile.objects.all()
    serializer_class = MemberProfileSerializer

    # Exact filtering
    filterset_fields = ['user', 'membership_id']

    # Search (partial match)
    search_fields = ['user', 'membership_id']

    # Ordering
    ordering_fields = ['user', 'membership_id']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        try:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

        except ProtectedError:
            return Response(
                {
                    "detail": "Cannot delete member because they have issued books."
                },
                status=status.HTTP_400_BAD_REQUEST
            )