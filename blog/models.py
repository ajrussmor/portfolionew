from django.db import models

class Brand(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now=False)
    description = models.TextField()
