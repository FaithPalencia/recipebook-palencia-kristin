from django.contrib import admin
from .models import Recipe, Profile, Ingredient, RecipeIngredient

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Profile)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)