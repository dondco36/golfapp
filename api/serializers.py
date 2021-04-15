from rest_framework import serializers
from GolfStatsApp import models

class GolfStatsAppSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'course',
            'score',
            'greens',
            'fairways',
            'putts',
        )
        model = models.User