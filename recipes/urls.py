from . import views
from django.urls import path

urlpatterns = [
    path("", views.RecipeList.as_view(), name='home'),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
]
