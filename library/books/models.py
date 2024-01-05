from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=100)
	birthdate = models.DateField()
	


class Book(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	isbn = models.CharField(max_length=13)






