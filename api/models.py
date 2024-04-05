from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Meal(models.Model):
    title = models.CharField(max_length=250)
    discription = models.TextField()


    def __str__(self) -> str:
        return self.title
    
    def num_rating(self):
        rating = Rating.objects.filter(meal=self)
        return len(rating)
    
    def avg(self):
        rating = Rating.objects.filter(meal=self)
        # avg = sum_rating/number of rating 
        rating_star = 0
        for x in rating:
            rating_star += x.stars
        if len(rating)>0:    
            return rating_star/len(rating)    
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