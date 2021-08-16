from django.db import models

# Create your models here.

class Search(models.Model):
    search = models.CharField(max_length=200)
    date_created = models.DateTimeField

    def __str__(self):
        return self.search

    class Meta:
        verbose_name_plural = "Searches"