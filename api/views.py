from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from .models import Rating,Meal
from .serailizers import RatingSerializer,MealSerializer,UserSerializer

# Create your views here.


class MealViewsets(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    # hold
    @action(methods=['POST',],detail=True)
    def rate_meal(self,request,pk=None):
        if 'stars' in request.data:
            meal = Meal.objects.get(id=pk)
            user = request.user
            stars = request.data['stars']

            # update Rating
            try:
                rating = Rating.objects.get(meal=meal.id,user=user.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating)
                json = {
                    'message' : 'Rating Updated',
                    'result' : serializer.data,
                }
                return Response(json,status=status.HTTP_200_OK)

            # create Rating
            except:
                rating = Rating.objects.create(user=user,meal=meal,stars=stars)
                serializer = RatingSerializer(rating)
                json = {
                    'message' : 'Rating Created',
                    'result' : serializer.data,
                }
                return Response(json,status=status.HTTP_201_CREATED)






class RatingViewsets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    def create(self, request, *args, **kwargs):
        response = {
            'response':'Created Denied from here',

        }
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, *args, **kwargs):
        response = {
            'response':'Updated Denied from here',

        }
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    
class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serailizer = self.get_serializer(data=request.data)
        serailizer.is_valid(raise_exception=True)
        self.perform_create(serailizer)
        token,crated = Token.objects.get_or_create(user=serailizer.instance)
        token_key = {
            'token' : token.key,
        }
        return Response(token_key,status=status.HTTP_200_OK)
    def list(self, request, *args, **kwargs):
        response = {
            'result' : 'Can not display users not allowed'
        }
        return Response(response,status=status.HTTP_204_NO_CONTENT)
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def register(request):
    if request.method == 'POST':
        serailizer = UserSerializer(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            token,created = Token.objects.get_or_create(user=serailizer.instance)
            token_key = {
            'token' : token.key,
        }
        return Response(token_key,status=status.HTTP_200_OK)
    