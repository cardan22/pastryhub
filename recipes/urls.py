from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path("my-recipes", views.MyRecipesList.as_view(), name="my_recipes"),
    path("add-recipe", views.AddRecipe.as_view(), name="add_recipe"),
    path(
        "update-recipe/<int:pk>", views.UpdateRecipe.as_view(), name="update"
        ),
    path("delete/<slug:pk>", views.DeleteRecipe.as_view(), name="delete"),
    path(
        "add-favorit-recipe/<int:id>", views.AddFavoriteRecipe.as_view(),
        name="add_favorite_recipe"),
    path(
        "favorite-recipes", views.FavoriteRecipesList.as_view(),
        name='favorite_recipes'),
    path("<slug:pk>", views.RecipeDetail.as_view(), name="recipe_detail"),
]
