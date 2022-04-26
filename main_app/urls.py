from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dolls/', views.dolls_index, name='index'),
    path('dolls/<int:doll_id>', views.dolls_detail, name='detail'),
    path('dolls/create/', views.DollCreate.as_view(), name='dolls_create'),
    path('dolls/<int:pk>/update/', views.DollUpdate.as_view(), name='dolls_update'),
    path('dolls/<int:pk>/delete/', views.DollDelete.as_view(), name='dolls_delete'),
    path('dolls/<int:doll_id>/add_seance/', views.add_seance, name='add_seance'),
    path('talismans/', views.TalismanList.as_view(), name='talismans_index'),
    path('talismans/<int:pk>/', views.TalismanDetail.as_view(), name='talismans_detail'),
    path('talismans/create/', views.TalismanCreate.as_view(), name='talismans_create'),
    path('talismans/<int:pk>/update/', views.TalismanUpdate.as_view(), name='talismans_update'),
    path('talismans/<int:pk>/delete/', views.TalismanDelete.as_view(), name='talismans_delete'),
] 