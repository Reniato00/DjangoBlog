from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    public = models.BooleanField()
    attachment_pdf =models.FileField(upload_to='pdfs/')
    image = models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class FormRequest(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
