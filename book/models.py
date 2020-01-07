from django.db import models

# book models here.
class Book(models.Model):
    name = models.CharField( max_length=50)
    picture = models.ImageField()
    author = models.CharField( max_length=50, default= 'anonymous')
    email = models.CharField(blank=True, max_length=50)
    describe = models.TextField(default ="Write")

    def __str__(self):
        return self.name
    