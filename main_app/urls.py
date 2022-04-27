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
    path('dolls/<int:doll_id>/add_photo/', views.add_photo, name='add_photo'),
    path('dolls/<int:doll_id>/assoc_talisman/<int:talisman_id>/', views.assoc_talisman, name='assoc_talisman'),
    path('dolls/<int:doll_id>/unassoc_talisman/<int:talisman_id>/', views.unassoc_talisman, name='unassoc_talisman'),
    path('talismans/', views.TalismanList.as_view(), name='talismans_index'),
    path('talismans/<int:pk>/', views.TalismanDetail.as_view(), name='talismans_detail'),
    path('talismans/create/', views.TalismanCreate.as_view(), name='talismans_create'),
    path('talismans/<int:pk>/update/', views.TalismanUpdate.as_view(), name='talismans_update'),
    path('talismans/<int:pk>/delete/', views.TalismanDelete.as_view(), name='talismans_delete'),
    path('accounts/signup/', views.signup, name='signup'),
] 