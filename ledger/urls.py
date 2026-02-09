from django.urls import path
from . import views

app_name = 'ledger'

urlpatterns = [
    path('', views.recipe_list),
    path('recipes/list', views.recipe_list),
    path('recipe/1', views.recipe_1),
    path('recipe/2', views.recipe_2),
]