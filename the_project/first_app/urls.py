from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('cost/', views.cost),
    path('add_member/', views.add_member),
    path('update_member/', views.update_member),
    path('del_member/', views.del_member)
]