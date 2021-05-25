from rest_framework import serializers
from GolfStatsApp import models

class GolfStatsAppSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'date',
            'course',
            'par',
            'score',
            'greens',
            'total_fairways',
            'fairways_hit',
            'putts',
            'greens_percentage',
            'fairways_percentage',
        )
        model = models.Round