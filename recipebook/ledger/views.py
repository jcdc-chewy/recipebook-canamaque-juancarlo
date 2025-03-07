from django.shortcuts import render
from .models import Recipe, RecipeIngredient


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ledger/recipe-list.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    return render(request, 'ledger/recipe.html', {'recipe': recipe, 'recipe_ingredients': recipe_ingredients})
