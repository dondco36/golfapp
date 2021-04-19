from rest_framework import serializers
from GolfStatsApp import models

class GolfStatsAppSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'user',
            'course',
            'score',
            'greens',
            'fairways',
            'putts',
        )
        model = models.Round