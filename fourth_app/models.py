from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_birth = models.DateField(auto_now=False)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Book(models.Model):
    CHOICES_GENRE =(
        ('comedy', 'Comedy'),
        ('tragedy', 'Tragedy'),
        ('drama', 'Drama')
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=2000)
    genre = models.CharField(max_length=50, choices=CHOICES_GENRE)
