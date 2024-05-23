from django.contrib import admin
from .models import Destination

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'best_time_to_visit', 'category', 'created_at', 'updated_at']
    search_fields = ['name', 'country']
    list_filter = ['category']
