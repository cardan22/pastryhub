from django import forms
from djrichtextfield.widgets import RichTextWidget
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

        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())

        labels = {
            "title": "Recipe Title",
            "baking_time": "Baking Time",
            "ingredients": "Ingredients",
            "instructions": "Instructions",
            "image": "Image",
            "image_alt": "Describe Image",
            "status": "Status"
        }
