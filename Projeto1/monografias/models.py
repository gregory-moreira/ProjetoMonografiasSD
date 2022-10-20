from datetime import datetime
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    lattes = models.URLField()
    google_scholar = models.URLField()
    research_gate = models.URLField()
    linkedin = models.URLField()
    orcid = models.URLField()
    github = models.URLField()

class CoAuthor(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    lattes = models.URLField()
    google_scholar = models.URLField()
    research_gate = models.URLField()
    linkedin = models.URLField()
    orcid = models.URLField()
    github = models.URLField()

class Student(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    lattes = models.URLField()
    google_scholar = models.URLField()
    research_gate = models.URLField()
    linkedin = models.URLField()
    orcid = models.URLField()
    github = models.URLField()

class Monography(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    advisor = models.ForeignKey(Author, on_delete=models.CASCADE)
    co_advisor = models.ForeignKey(CoAuthor, on_delete=models.CASCADE)
    date = models.DateField()
    summary = models.CharField(max_length=100)
    key_words = models.CharField()
    university = models.CharField(max_length=80)
    course = models.CharField(max_length=50)
    monography = models.URLField()

class MonographyAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    monography = models.ForeignKey(Monography, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} -> {self.monography}'

class MonographyCoAuthor(models.Model):
    co_author = models.ForeignKey(CoAuthor, on_delete=models.CASCADE)
    monography = models.ForeignKey(Monography, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.co_author} -> {self.monography}'

class MonographyStudent(models.Model):    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    monography = models.ForeignKey(Monography, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student} -> {self.monography}'





