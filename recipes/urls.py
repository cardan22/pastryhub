from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path("", views.RecipeList.as_view(), name='home'),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
]
