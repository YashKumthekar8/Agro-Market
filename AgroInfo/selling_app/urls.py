from django.urls import path
from . import views

urlpatterns = [
    path('', views.plants, name='plants'),
    path('Fertilizers.html/', views.fertilizers, name="fertilizers" ),
    path('Fertilizers-Name.html/<str:val>/', views.fertilizers_name, name="fertilizers_name" ),
    path('Flower.html/', views.flower, name="flower" ),
    path('Flower-City.html/<str:val>/', views.flower_city1, name="flower_city1" ),
    path('Flower-Name.html/<str:val>/', views.flower_name, name="flower_name" ),
    path('Fruit.html/', views.fruit, name="fruit" ),
    #  path('Fruit-City.html/', views.fruit_city, name="fruit_city" ),
    path('Fruit-City.html/<str:val>/', views.fruit_city1, name="fruit_city1" ),
    path('Fruit-Name.html/<str:val>/', views.fruit_name, name="fruit_name" ),
    path('Vegetable.html/', views.vegetable, name="vegetable" ),
    # path('Vegetable-City.html/', views.vegetable_city, name="vegetable_city" ),
    path('Vegetable-City.html/<str:val>/', views.vegetable_city1, name="vegetable_city1" ),
    path('Vegetable-Name.html/<str:val>/', views.vegetable_name, name="vegetable_name" ),    
]