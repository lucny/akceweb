from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # zobrazení seznamu akcí
    path('create/', views.AkceCreateView.as_view(), name='akce_create'),
    path('detail/<int:pk>/', views.AkceDetailView.as_view(), name='akce_detail'),
    path('detail/<int:pk>/update/', views.AkceUpdateView.as_view(), name='akce_update'),
    path('detail/<int:pk>/delete/', views.AkceDeleteView.as_view(), name='akce_delete'),
]