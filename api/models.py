from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Meal(models.Model):
    title = models.CharField(max_length=250)
    discription = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    def num_reviews(self):
        rating = Rating.objects.filter(meal=self)
        return len(rating)
    
    def avg(self):
        rating = Rating.objects.filter(meal=self)
        num_stars = 0
        for x in rating:
            num_stars += x.stars
        if len(rating) > 0:    
            return num_stars/len(rating)    
        return 0


class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)     
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self) -> str:
        return str(self.meal)
    class Meta:
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal'),) 