from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic, View
from django.views.generic.edit import CreateView
from .models import Recipe
from .forms import RecipeForm


class RecipeList(generic.ListView):
    """ View all recipes"""
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-posted_date")
    template_name = "index.html"
    paginate_by = 6


class AddRecipe(LoginRequiredMixin, CreateView):
    """Add recipe view"""

    template_name = "add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/my_recipes/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddRecipe, self).form_valid(form)
