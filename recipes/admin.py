from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'baking_time', 'image')
    summernote_fields = ('ingredients', 'instructions')
    list_filter = ('status', 'posted_date')
