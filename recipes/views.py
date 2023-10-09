from django.shortcuts import render
from django.views import generic, View
from .models import Recipe


class RecipeList(generic.ListView):
    """ View all recipes"""
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-posted_date")
    template_name = "index.html"
    paginate_by = 6
