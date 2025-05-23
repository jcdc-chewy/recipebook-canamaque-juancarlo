from django.urls import path
from . import views

urlpatterns = [
    path('recipes/list', views.recipe_list, name='recipe_list'),
    path('recipe/add/', views.recipe_add, name='recipe_add'),
    path('recipe/<str:recipe_name>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:pk>/add_image/', views.add_recipe_image, name='add_recipe_image'),
]
