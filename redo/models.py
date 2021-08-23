from django.db import models

class Total(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now=False)
    description = models.TextField()

    # def __str__(self):
    #     return self.title, self.description
