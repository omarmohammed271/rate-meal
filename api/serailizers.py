from rest_framework import serializers
from .models import Meal,Rating
# uuid
# slug
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id','title','discription']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'         