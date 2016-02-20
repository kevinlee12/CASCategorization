from rest_framework import serializers
from journal.models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    """Activity model serializer"""
    class Meta:
        model = Activity
        fields = ('name', 'description', 'activity_type', 'learning_obj',
                  'start_date', 'end_date', 'entries')
