from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True)
    duration = models.IntegerField()

    def __str__(self):
        return self.title
