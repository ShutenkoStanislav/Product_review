from django.urls import path
from reviews import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product_list", views.product_list, name="product_list")
]