from django.urls import path

from . import views

urlpatterns = [
    path('', views.SearchMonographyView.as_view(), name='index'),
    path('create-patient/', views.MonographyView.as_view(), name='monography'),
    path('add-existent-patient/', views.CoAuthorView.as_view(), name='co-author'),
    path('register-symptoms/<int:pk>/', views.StudentView.as_view(), name='student'),
    path('create-symptom/<int:pk>/', views.AuthorView.as_view(), name='author'),
]