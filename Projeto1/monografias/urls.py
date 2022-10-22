from django.urls import path

from . import views

urlpatterns = [
    path('', views.SearchMonographyView.as_view(), name='index'),
    # path('create-author/', views.CreateAuthorView.as_view(), name='create-author'),
    path('create-author/', views.AuthorView.as_view(), name='create-author'),
    # path('create-co-author/', views.CreateCoAuthorView.as_view(), name='create-co-author'),
    path('create-co-author/', views.CoAuthorView.as_view(), name='create-co-author'),
    # path('create-student/', views.CreateStudentView.as_view(), name='create-student'),
    path('create-student/', views.StudentView.as_view(), name='create-student'),
    # path('create-co-author/', views.CreateCoAuthorView.as_view(), name='create-co-author'),
    # path('add-existent-patient/', views.CoAuthorView.as_view(), name='co-author'),
    # path('register-symptoms/<int:pk>/', views.StudentView.as_view(), name='student'),
    # path('create-symptom/<int:pk>/', views.AuthorView.as_view(), name='author'),
]