from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny

from .models import MemberProfile
from .serializers import MemberProfileSerializer


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