from django.shortcuts import render
from .models import Recipe, RecipeIngredient


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ledger/recipe-list.html', {'recipes': recipes})


def recipe_detail(request, recipe_name):
    recipe = Recipe.objects.get(name=recipe_name)
    recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    return render(request, 'ledger/recipe.html', {'recipe': recipe, 'recipe_ingredients': recipe_ingredients})
