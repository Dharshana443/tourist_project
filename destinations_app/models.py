# destinations_app/models.py
from django.db import models


class TouristDestination(models.Model):
    WEATHER_CHOICES = [
        ("SUNNY", 'Sunny'),
        ("CLOUDY", 'Cloudy'),
        ("RAINY", 'Rainy'),
        ("SNOWY", 'Snowy'),
    ]

    place_name = models.CharField(max_length=100)
    weather = models.CharField(max_length=20, choices=WEATHER_CHOICES)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    google_map_link = models.URLField(max_length=500)
    description = models.TextField()
    destination_img = models.ImageField(upload_to='destination_images/', null=True, blank=True)

    def __str__(self):
        return self.place_name