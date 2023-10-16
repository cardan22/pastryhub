from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .models import Recipe, FavoriteRecipe
from .forms import RecipeForm


class RecipeList(ListView):
    """
    View to display a list of all published recipes.

    This view retrieves all recipes with 'status' set to 1
    (published) and orders them by their posting date.
    """

    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-posted_date")
    template_name = "index.html"
    paginate_by = 6


class RecipeDetail(DetailView):
    """
    View to display the details of a recipe.

    This view retrieves the details of a single recipe using its primary key.
    """

    model = Recipe
    template_name = "recipe_detail.html"
    context_object_name = "recipe"


class AddRecipe(LoginRequiredMixin, CreateView):
    """
    View to add a new recipe.

    This view allows authenticated users to create and submit a new recipe.
    """

    template_name = "add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/my_recipes/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddRecipe, self).form_valid(form)


class UpdateRecipe(LoginRequiredMixin, UpdateView):
    """
    View to update an existing recipe.

    This view allows authenticated users to update an already submitted recipe.
    """

    model = Recipe
    form_class = RecipeForm
    template_name = "update_recipe.html"
    success_url = "/my_recipes/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(UpdateView, self).form_valid(form)


class MyRecipesList(LoginRequiredMixin, ListView):
    """
    View to display a list of recipes created by the logged-in user.

    This view retrieves and displays all recipes
    created by the currently logged-in user.
    """

    model = Recipe
    queryset = Recipe.objects.order_by("-posted_date")
    template_name = "my_recipes.html"
    paginate_by = 8

    def get_queryset(self):
        queryset = Recipe.objects.filter(
            author__id=self.request.user.id).order_by("-posted_date")
        return queryset
