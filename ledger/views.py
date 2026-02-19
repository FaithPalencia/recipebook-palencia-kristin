from django.shortcuts import render
from .models import Recipe

# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request,'ledger/recipe_list.html',{'recipes':recipes})

def recipe_detail(request,id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'ledger/recipe_ingredients.html',{'recipe':recipe})