from django.urls import path, include
from . import views


urlpatterns = [
    path('owners/', views.owner_list, name='owner_list'),
    path('owners/create/', views.owner_create, name='owner_create'),
    path('owners/<int:pk>/edit/', views.owner_edit, name='owner_edit'),
    path('owners/<int:pk>/delete/', views.owner_delete, name='owner_delete'),
    path('cars/', views.car_list, name='car_list'),
    path('cars/create/', views.car_create, name='car_create'),
    path('cars/<int:pk>/edit/', views.car_edit, name='car_edit'),
    path('cars/<int:pk>/delete/', views.car_delete, name='car_delete'),
    path('accounts/', include('allauth.urls')),
]
