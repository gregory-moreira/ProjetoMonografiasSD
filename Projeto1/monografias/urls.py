from django.urls import path

from . import views

urlpatterns = [
    path('', views.SearchMonographyView.as_view(), name='index'),
    # path('create-author/', views.CreateAuthorView.as_view(), name='create-author'),
    path('create-advisor/', views.AdvisorView.as_view(), name='create-advisor'),
    # path('create-co-author/', views.CreateCoAuthorView.as_view(), name='create-co-author'),
    path('create-co-advisor/', views.CoAdvisorView.as_view(), name='create-co-advisor'),
    # path('create-student/', views.CreateStudentView.as_view(), name='create-student'),
    path('create-author/', views.AuthorView.as_view(), name='create-author'),
    path('create-monography/', views.MonographyView.as_view(), name='create-monography'),

    # path('create-co-author/', views.CreateCoAuthorView.as_view(), name='create-co-author'),
    # path('add-existent-patient/', views.CoAuthorView.as_view(), name='co-author'),
    # path('register-symptoms/<int:pk>/', views.StudentView.as_view(), name='student'),
    # path('create-symptom/<int:pk>/', views.AuthorView.as_view(), name='author'),
]