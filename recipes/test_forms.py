from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe, FavoriteRecipe
from cloudinary.models import CloudinaryField

class RecipeModelTest(TestCase):
    """Set up a test user and a sample recipe for testing."""
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

    def test_recipe_title(self):
        """ Test the title of a Recipe model."""
        recipe = Recipe.objects.get(id=self.recipe.id)
        self.assertEqual(recipe.title, 'Test Recipe')

    def test_recipe_author(self):
        """Test the author of a Recipe model."""
        recipe = Recipe.objects.get(id=self.recipe.id)
        self.assertEqual(recipe.author, self.user)

    def test_recipe_str(self):
        """Test the string representation of a Recipe model."""
        recipe = Recipe.objects.get(id=self.recipe.id)
        self.assertEqual(str(recipe), 'Test Recipe')