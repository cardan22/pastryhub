from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path("my_recipes/", views.MyRecipesList.as_view(), name="my_recipes"),
    path("add_recipe/", views.AddRecipe.as_view(), name="add_recipe"),
    path(
        "update_recipe/<int:pk>/", views.UpdateRecipe.as_view(), name="update"
        ),
    path("<slug:pk>/", views.RecipeDetail.as_view(), name="recipe_detail"),
]
