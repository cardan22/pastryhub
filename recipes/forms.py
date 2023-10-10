from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """Form to create a recipe"""

    class Meta:
        model = Recipe

        fields = [
            "title",
            "baking_time",
            "ingredients",
            "instructions",
            "image",
            "image_alt",
            "status",
        ]

        labels = {
            "title": "Recipe Title",
            "baking_time": "Baking Time",
            "ingredients": "Ingredients",
            "instructions": "Instructions",
            "image": "Image",
            "image_alt": "Describe Image",
            "status": "Status"
        }
