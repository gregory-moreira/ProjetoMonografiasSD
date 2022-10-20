from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from .models import Monography, Author, CoAuthor, Student

# Create your views here.
class AuthorView(View):
  def get(self, request):
    return render(request, 'monografias/author.html')
  
  def post(self, reqeust):
    data = reqeust.POST
    Author.objects.create(
      name=data['name'], 
      course=data['course'], 
      university=data['university'], 
      email=data['email'], 
      lattes=data['lattes'], 
      google_scholar=data['google_scholar'], 
      research_gate=data['research_gate'], 
      linkedin=data['linkedin'], 
      orcid=data['orcid'], 
      github=data['github']
    )
    redirect('index')

class CoAuthorView(View):
  def get(self, request):
    return render(request, 'monografias/co-author.html')
  
  def post(self, reqeust):
    data = reqeust.POST
    CoAuthor.objects.create(
      name=data['name'], 
      course=data['course'], 
      university=data['university'], 
      email=data['email'], 
      lattes=data['lattes'], 
      google_scholar=data['google_scholar'], 
      research_gate=data['research_gate'], 
      linkedin=data['linkedin'], 
      orcid=data['orcid'], 
      github=data['github']
    )
    redirect('index')

class StudentView(View):
  def get(self, request):
    return render(request, 'monografias/student.html')
  
  def post(self, reqeust):
    data = reqeust.POST
    Student.objects.create(
      name=data['name'], 
      course=data['course'], 
      university=data['university'], 
      email=data['email'], 
      lattes=data['lattes'], 
      google_scholar=data['google_scholar'], 
      research_gate=data['research_gate'], 
      linkedin=data['linkedin'], 
      orcid=data['orcid'], 
      github=data['github']
    )
    redirect('index')

class MonographyView(View):
  def get(self, request):
    author = Author.objects.all()
    co_author = CoAuthor.objects.all()
    student = Student.objects.all()
    return render(request, 'monografias/monography.html', {
      'author': author, 'co_author': co_author, 'student': student
    })
  def post(self, request):
    pass

class SearchMonographyView(View):
  def get(self, request):
    return render(request, 'index.html')

  def post(self, request):
    search = request.POST['search']
    monographys = Monography.objects.filter(Q(title__icontains=search) | Q(university__icontains=search) | Q(summary__icontains=search))

    return render(request, 'monografias/search.html', { "monographys": monographys })
