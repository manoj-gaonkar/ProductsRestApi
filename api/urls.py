from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    path('allproducts/',views.getProducts),
    path('addproduct/',views.addProducts),
    path('deleteproduct/<int:pk>',views.deleteProduct),
]
