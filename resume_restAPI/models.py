from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    education = models.TextField()
    experience = models.TextField()
    resume_file = models.FileField(upload_to='resumes/')
