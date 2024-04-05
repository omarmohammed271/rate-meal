from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Meal,Rating
# uuid
# slug
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id','title','discription','avg','num_reviews']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'     

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs  = {'password': {'write_only': True, 'required': True}}

