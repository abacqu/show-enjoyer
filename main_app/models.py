from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('categories_detail', kwargs={'pk': self.id})


class Show(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    songs = models.TextField(max_length=250)
    reflection = models.TextField(max_length=250)
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'show_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for show_id: {self.show_id} @{self.url}"