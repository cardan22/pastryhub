from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Recipe, FavoriteRecipe
from .forms import RecipeForm
from django.contrib.auth import get_user_model

class RecipeFormTest(TestCase):
    """Set up a test user for the RecipeForm test."""
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_recipe_form_valid(self):
        """Test the validity of the RecipeForm."""
        form = RecipeForm(data={
            'title': 'Test Recipe',
            'baking_time': 60,
            'ingredients': 'Test ingredients',
            'instructions': 'Test instructions',
            'image': SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
            'image_alt': 'Test image alt text',
            'status': 0,
        })
        form.instance.author = self.user

        self.assertTrue(form.is_valid())

class FavoriteRecipeModelTest(TestCase):
    """Set up a test user, recipe, and favorite recipe for testing."""
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            author=self.user,
            baking_time=60,
            instructions="Test instructions",
            ingredients="Test ingredients",
            image="test_image.jpg",
            image_alt="Test image alt text",
            status=0
        )
        self.favorite_recipe = FavoriteRecipe.objects.create(
            user=self.user,
            recipe=self.recipe
        )

    def test_favorite_recipe_user(self):
        """Test the user associated with a FavoriteRecipe."""
        favorite_recipe = FavoriteRecipe.objects.get(id=self.favorite_recipe.id)
        self.assertEqual(favorite_recipe.user, self.user)
