from rest_framework import serializers ,status
from .models import *

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'

class Mealserializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class Ratingserializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

