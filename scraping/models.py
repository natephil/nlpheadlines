from django.db import models
from django.utils import timezone

# Create your models here.

class Headline(models.Model):
    source = models.CharField(max_length=250, default="default_value")
    title = models.CharField(max_length=500)
    # published_date = models.CharField(max_length=250)
    published_date = models.DateTimeField()
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['published_date']
    class Admin:
        pass