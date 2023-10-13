from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "baking_time", "image", "status", "posted_date")
    list_filter = ("status", "posted_date")
