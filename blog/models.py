from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=30)
    writer = models.CharField(max_length=10)
    body = models.TextField()
    

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def summary(self):
        return self.body[:100]