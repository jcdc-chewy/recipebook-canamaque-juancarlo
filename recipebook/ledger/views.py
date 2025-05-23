from django.shortcuts import render, redirect
from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientFormSet
from django.contrib.auth.decorators import login_required


@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()

    return render(request, 'ledger/recipe-list.html', {'recipes': recipes})

@login_required
def recipe_detail(request, recipe_name):
    recipe = Recipe.objects.get(name=recipe_name)
    recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    recipe_images = recipe.images.all()

    return render(request, 'ledger/recipe.html', {
        'recipe': recipe,
        'recipe_ingredients': recipe_ingredients,
        'recipe_images': recipe_images,
        'author': recipe.author,
    })


@login_required
def recipe_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        formset = RecipeIngredientFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            formset.instance = recipe
            formset.save()
            return redirect('recipe_detail', recipe_name=recipe.name)
    else:
        form = RecipeForm()
        formset = RecipeIngredientFormSet()

    return render(request, 'ledger/recipe_add.html', {
        'form': form,
        'formset': formset,
    })
