from django.db import models

# Create your models here.

class Encrypt(models.Model):
    message = models.TextField()
    key = models.CharField(max_length=100)
    token = models.TextField()
    def __str__(self):
        return self.message
    
class Decrypt(models.Model):
    token = models.TextField()
    key = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.message


