from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Recipe, FavoriteRecipe

class TestViews(TestCase):

    def test_home_page(self):
        """Test that the home page renders the correct HTML page"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def setUp(self):
        """Create a test login user and a sample recipe for testing"""

        email = "testuser@example.com"
        usrnm = "testuser"
        pswd = "SecurePass123"
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            email=email, username=usrnm, password=pswd
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
        logged_in = self.client.login(username=usrnm, password=pswd)
        self.assertTrue(logged_in)

    def test_add_recipe(self):
        """Test if add_recipe page renters correctly """
        response = self.client.get('/add-recipe')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')

    def test_my_recipes(self):
        """Test if my_recipes page renters correctly """
        response = self.client.get('/my-recipes')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_recipes.html')
