from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
 
    list_display = ('name',)
    search_fields = ('name',)


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [RecipeImageInline]


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
