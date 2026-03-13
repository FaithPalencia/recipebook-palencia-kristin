from django.contrib import admin
from .models import Recipe, Profile, RecipeIngredient, RecipeImage, Ingredient

# Register your models here.
class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeImageInline, RecipeIngredientInline,]

admin.site.register(Profile)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeImage)
admin.site.register(Recipe, RecipeAdmin)