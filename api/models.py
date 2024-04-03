from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Meal(models.Model):
    title = models.CharField(max_length=250)
    discription = models.TextField()

    def __str__(self) -> str:
        return self.title

class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)     
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self) -> str:
        return str(self.meal)