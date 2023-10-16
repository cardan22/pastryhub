from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, DetailView
from .models import Recipe, FavoriteRecipe
from .forms import RecipeForm


class RecipeList(ListView):
    """View all recipes"""

    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-posted_date")
    template_name = "index.html"
    paginate_by = 6


class RecipeDetail(DetailView):
    """View to display details of a recipe."""

    model = Recipe
    template_name = "recipe_detail.html"
    context_object_name = "recipe"


class AddRecipe(LoginRequiredMixin, CreateView):
    """Add recipe view"""

    template_name = "add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/my_recipes/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddRecipe, self).form_valid(form)


class MyRecipesList(LoginRequiredMixin, ListView):
    """ My Recipes view """

    model = Recipe
    queryset = Recipe.objects.order_by("-posted_date")
    template_name = "my_recipes.html"
    paginate_by = 8

    def get_queryset(self):
        queryset = Recipe.objects.filter(
            author__id=self.request.user.id).order_by("-posted_date")
        return queryset
