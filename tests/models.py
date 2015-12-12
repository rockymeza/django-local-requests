from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)


class Book(models.Model):
    author = models.ForeignKey('Author', related_name='books')

    title = models.CharField(max_length=500)
