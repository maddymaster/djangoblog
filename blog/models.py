from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 300)
    body = models.TextField()
    date = models.DateTimeField()
    file = models.FileField()

    def __str__(self):
        return self.title
