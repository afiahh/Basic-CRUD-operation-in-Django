from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('diary_list/', views.diary_list, name='diary_list'),
    path('new/', views.diary_create, name='diary_create'),
    path('edit/<int:pk>/', views.diary_update, name='diary_update'),
    path('diary/<int:pk>/delete/', views.diary_delete, name='diary_delete'),
    path('<int:pk>/read/', views.diary_read, name='diary_read'),
]
