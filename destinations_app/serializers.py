# destinations_app/serializers.py
from rest_framework import serializers
from .models import TouristDestination


class TouristDestinationSerializer(serializers.ModelSerializer):
    destination_img = serializers.ImageField(required=False)

    class Meta:
        model = TouristDestination
        fields = "__all__"