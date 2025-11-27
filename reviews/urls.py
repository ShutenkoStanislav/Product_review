from django.urls import path
from reviews import views



urlpatterns = [
    path("", views.home, name="home"),
    path("product_list/", views.product_list, name="product_list"),
    path("product/<int:product_id>/add_review/", views.add_review, name="add_review"),
    path("review/<int:pk>/", views.product_details, name="product_details"),  
]