from .views import DashboardView
from django.urls import path

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'), # APIView URL
]
