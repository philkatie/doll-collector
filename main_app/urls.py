from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dolls/', views.dolls_index, name='index'),
    path('dolls/<int:doll_id>', views.dolls_detail, name='detail'),
] 