from django.db import models

# Create your models here.
class List(models.Model):
    item = models.CharField(max_length = 264)
    completed = models.BooleanField()
    def __str__(self):
        return self.item
