from rest_framework import serializers ,status
from .models import *

# class GuestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Guest
#         fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ("id","title" , "description" , "no_of_ratings" , "avg_rating")

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

