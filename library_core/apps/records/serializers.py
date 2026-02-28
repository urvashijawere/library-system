from rest_framework import serializers
from .models import IssueRecord

class IssueRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueRecord
        fields = "__all__"
