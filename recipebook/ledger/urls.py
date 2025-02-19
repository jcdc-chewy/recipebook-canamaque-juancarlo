from django.urls import path
from . import views

urlpatterns = [
    path('recipes/list', views.page_one, name='page_one'),
    path('recipe/1', views.page_two, name='page_two'),
    path('recipe/2', views.page_three, name='page_three'),
]
