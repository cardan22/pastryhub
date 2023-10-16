from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from djrichtextfield.models import RichTextField

STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):

    """
    A recipe model that enables users to create,
    view, update, and delete recipes.
    """

    title = models.CharField(max_length=200, unique=True, blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="add_recipe"
    )
    baking_time = models.PositiveIntegerField(blank=False)
    instructions = RichTextField(max_length=10000, null=False, blank=False)
    ingredients = RichTextField(max_length=10000, null=False, blank=False)
    image = CloudinaryField("image", default="placeholder", null=False)
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    posted_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return self.title


class FavoriteRecipe(models.Model):
    """
    Model representing a user's favorite recipe.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'recipe')
