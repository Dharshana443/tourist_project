# destinations_app/admin.py
from django.contrib import admin
from .models import TouristDestination

# Unregister if already registered (to avoid conflicts)
try:
    admin.site.unregister(TouristDestination)
except:
    pass

# Register with minimal configuration
@admin.register(TouristDestination)
class TouristDestinationAdmin(admin.ModelAdmin):
    fields = ['place_name', 'weather', 'state', 'district',
              'google_map_link', 'description', 'destination_img']