from django.contrib import admin
from django.urls import path , include
from API.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('MealList',MealList)
# router.register('GustList',GustList)
router.register('RatingList',RatingList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),      
]
