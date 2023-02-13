from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from django.contrib.auth.models import User

from rest_framework.decorators import action
from rest_framework.response import Response


class MealList(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(detail=True, methods=['post'])
    def rate_meal(self, request, pk):
        """
            if  (create or update) :
                body::
            else:
                Error
        """
        if 'stars' in request.data:
            meal = Meal.objects.get(id=pk)
            username = request.data['username']
            user = User.objects.get(username=username)
            # Update : you must pass all data of model to a success put
            try:
                queryRating = Rating.objects.get(meal=meal.id, user=user.id)
                serializer = RatingSerializer(
                    instance=queryRating, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    json = {
                        'message': "Done , Update",
                        'result': serializer.data,
                    }
                    return Response(json,  status=status.HTTP_200_OK)
                else:
                    json = {
                        'message': "Update ,It didn't work because of an error "
                    }
                    return Response(json, status=status.HTTP_400_BAD_REQUEST)
            except:
                # Create
                serializer = RatingSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    json = {
                        'message': "Done , Created",
                        'result': serializer.data,
                    }
                    return Response(json,  status=status.HTTP_200_OK)
                else:
                    json = {
                        'message': "Create,It didn't work because of an error",
                    }
                    return Response(json, status=status.HTTP_400_BAD_REQUEST)

        else:
            json = {
                'message': "This request is error"
            }
            Response(json, status=status.HTTP_400_BAD_REQUEST)


class RatingList(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
