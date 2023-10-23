from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView
    )
from .models import Recipe, FavoriteRecipe
from .forms import RecipeForm


class RecipeList(ListView):
    """
    View to display a list of all published recipes.

    This view retrieves all recipes with status set to 1
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            recipe = self.object
            favorite = FavoriteRecipe.objects.filter(
                user=self.request.user, recipe=recipe).exists(
                )
            context['favorite'] = favorite
        return context


class AddRecipe(LoginRequiredMixin, CreateView):
    """
    View to add a new recipe.

    This view allows authenticated users to create and submit a new recipe.
    """

    template_name = "add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy("my_recipes")

    def form_valid(self, form):
        form.instance.author = self.request.user
        msg = "Your Recipe was added successfully"
        messages.add_message(self.request, messages.SUCCESS, msg)
        return super(AddRecipe, self).form_valid(form)


class UpdateRecipe(LoginRequiredMixin, UpdateView):
    """
    View to update an existing recipe.

    This view allows authenticated users to update an already submitted recipe.
    """

    model = Recipe
    form_class = RecipeForm
    template_name = "update_recipe.html"
    success_url = reverse_lazy("my_recipes")

    def form_valid(self, form):
        form.instance.author = self.request.user
        msg = "Your Recipe was updated successfully"
        messages.add_message(self.request, messages.SUCCESS, msg)
        return super(UpdateView, self).form_valid(form)

    def get_object(self, queryset=None):
        """
        Retrieve the recipe object to update
        and check if it belongs to the user.
        """
        obj = super(UpdateRecipe, self).get_object(queryset)
        get_object_or_404(Recipe, author=self.request.user, id=obj.id)

        return obj


class DeleteRecipe(LoginRequiredMixin, DeleteView):
    """
    This view allows an authenticated user to delete a recipe.
    """

    model = Recipe
    template_name = "delete_recipe.html"
    success_url = reverse_lazy("my_recipes")

    def delete(self, request, *args, **kwargs):
        msg = "Your Recipe was deleted successfully"
        messages.add_message(self.request, messages.SUCCESS, msg)
        return super(DeleteView, self).delete(request, *args, **kwargs)


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


class AddFavoriteRecipe(LoginRequiredMixin, ListView):
    """
    View for adding/removing recipes from user's favorites.

    Allows authenticated users to add or remove recipes from their favorites.
    If already a favorite, it's removed; otherwise, it's added.
    """

    def get(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        favorite, created = FavoriteRecipe.objects.get_or_create(
            user=request.user, recipe=recipe
            )

        if not created:
            favorite.delete()
            msg = "This recipe was removed from your favorites"
            messages.warning(request, msg)
        else:
            msg = "This recipe was added to your favorites."
            messages.success(request, msg)

        return redirect(request.META.get('HTTP_REFERER'))


class FavoriteRecipesList(LoginRequiredMixin, ListView):
    """
    View to display a list of the user's favorite recipes.

    This view retrieves and displays a list of recipes that the logged-in user
    has marked as their favorite recipes."""

    model = FavoriteRecipe
    template_name = 'favorite_recipes.html'
    context_object_name = 'favorite_recipes'

    def get_queryset(self):
        return FavoriteRecipe.objects.filter(user=self.request.user)
