from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants/',  views.RestaurantList.as_view(), name="restaurants_index"),
    path('accounts/signup/', views.signup, name='signup'),
    path('restaurants/<int:pk>/', views.RestaurantDetail.as_view(), name='restaurants_detail'),
    path('restaurants/<int:restaurant_id>/menu/<int:pk>/', views.MenuItemDetail.as_view(), name='menuitems_detail'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipes_detail'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipes/<int:recipe_id>/add_instruction/', views.add_instruction, name='add_instructions'),
    path('recipes/<int:recipe_id>/add_ingredient/', views.add_ingredient, name='add_ingredients'),
]