from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Code taken from "theRecipeCollective"
# bySandraBergstrom with some modifications.

# class LikedManager(models.Manager):
#     def get_queryset(self, user):
#         return super().get_queryset().filter(likes=user)

# Status for user to set if recipe should be draft or pubilished.


STATUS = ((0, "Draft"), (1, "Published"))


"""
A recipe model that enables users to create, view, update, and delete recipes.
"""


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="add_recipe"
    )
    baking_time = models.PositiveIntegerField(blank=False)
    ingredients = models.TextField(max_length=10000, null=False, blank=False)
    instructions = models.TextField(max_length=10000, null=False, blank=False)
    image = CloudinaryField("image", default="placeholder", null=False)
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    posted_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="like", default=None, blank=True)
    # liked_recipes = LikedManager()

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return self.title
