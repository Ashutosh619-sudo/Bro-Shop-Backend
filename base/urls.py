from django.urls import path
from . import views

urlpatterns = [
    # path('', views.getRoutes,name="routes"),
    path('products', views.getProducts,name="getproducts"),
    path('product/<str:pk>/', views.getProduct,name="getproduct"),
]