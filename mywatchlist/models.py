from django.db import models

# Create your models here.
class MyWatchlistModel(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length = 255)
    rating = models.IntegerField(
            default = 1, 
            validators =[
                MaxValueValidator(100),
                MinValueValidator(1)
                ]
            )
    release_date = models.DateField()
    review = models.TextField()

