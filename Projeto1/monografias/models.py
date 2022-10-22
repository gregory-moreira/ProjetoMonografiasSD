from datetime import datetime
from email.policy import default
from random import choices
from django.db import models
    

class User(models.Model):
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

    type = (
        ("E", "Estudante"),
        ("O", "Orientador"),
        ("C", "Co-Orientador"),
    )

    user_type = models.CharField(max_length=30, choices=type, default="E")

    def __str__(self):
        return self.name

class Monography(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    advisor = models.ForeignKey(User, on_delete=models.CASCADE)
    co_advisor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    summary = models.CharField(max_length=100)
    key_words = models.CharField(max_length=100)
    university = models.CharField(max_length=80)
    course = models.CharField(max_length=50)
    monography = models.URLField()

    def __srt__(self):
        return self.title


