from django.db import models

# Create your models here.
class update(models.Model):
    content = models.TextField()
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.content

class aboutus(models.Model):
    content = models.CharField(max_length =100)
    date = models.DateTimeField(auto_now_add =False)

    def __str__(self):
        return self.content

class Astroh(models.Model):
    content = models.CharField(max_length =100)
    date = models.DateTimeField(auto_now_add =False)

    def __str__(self):
        return self.content

class Portfolio(models.Model):
    content = models.CharField(max_length =100)
    date = models.DateTimeField(auto_now_add =False)

    def __str__(self):
        return self.content


class Review(models.Model):
    title = models.CharField(max_length =40)
    content = models.CharField(max_length =100)
    date = models.DateTimeField(auto_now_add =False)

    def __str__(self):
        return self.content

class Contacts(models.Model):
    title = models.CharField(max_length =40)
    content = models.CharField(max_length =100)
    date = models.DateTimeField(auto_now_add =False)

    def __str__(self):
        return self.title
