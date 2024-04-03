from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
app_name = 'api'

router = DefaultRouter()
router.register('meal',views.MealViewsets)
router.register('rating',views.RatingViewsets)


urlpatterns = [
    path('',include(router.urls)),
]
