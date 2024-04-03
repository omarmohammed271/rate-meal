from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from .models import Rating,Meal
from .serailizers import RatingSerializer,MealSerializer

# Create your views here.


class MealViewsets(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    # hold
    @action(methods=['POST',],detail=True)
    def rate_meal(self,request):
        if 'stars' in request.data:
            meal = request.data['meal']
            username = request.data['username']
            user = User.objects.get(username=username)
            stars = request.data['stars']

            # update Rating
            try:
                rating = Rating.objects.get(meal=meal,user=user)
                rating.stars = stars
                rating.save()
                json = {
                    'message' : 'Rating Updated'
                }
                return Response(json,status=status.HTTP_200_OK)

            # create Rating
            except:
                rating = Rating.objects.create(user=user,meal=meal,stars=stars)
                json = {
                    'message' : 'Rating Created'
                }
                return Response(json,status=status.HTTP_201_CREATED)




class RatingViewsets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer