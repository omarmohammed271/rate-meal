from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
app_name = 'api'

router = DefaultRouter()
router.register('meal',views.MealViewsets)
router.register('rating',views.RatingViewsets)
router.register('users',views.UserViewset)


urlpatterns = [
    path('',include(router.urls)),
    path('register/',views.register)
]
