from django.db import models

# Create your models here.

class Menus(models.Model):
    title = models.CharField(max_length=250)
    descriptions = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    