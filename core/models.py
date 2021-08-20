from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    message = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)