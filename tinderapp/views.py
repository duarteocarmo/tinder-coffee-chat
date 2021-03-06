from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers

class HelloView(APIView):
    """
    Welcome to the api :) 
    """
    def get(self, request):
        return Response({"status":"active"})

class UserListView(generics.ListAPIView):
    """
    Get a list of all users that are registered, 
    and their availability. 
    """
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class InterestListView(generics.ListAPIView):
    """
    Get a list of all users that are registered, 
    and their availability. 
    """
    queryset = models.Interest.objects.all()
    serializer_class = serializers.InterestSerializer


class CurrentUserView(APIView):
    def get(self, request):
        serializer = serializers.UserSerializer(request.user)
        return Response(serializer.data)

class GetAvailableUsers(APIView):
    def get(self, request):
        current_user = request.user
        available_users = models.CustomUser.objects.filter(
            available=True
        ).exclude(id=current_user.id)
        return Response(available_users)


class ToggleAvailability(APIView):
    def get(self, request):
        current_user = request.user
        user_object = models.CustomUser.objects.get(id=current_user.id)
        current_availability = user_object.available
        new_availability = not current_availability
        models.CustomUser.objects.filter(id=current_user.id).update(
            available=new_availability
        )
        serializer = serializers.UserSerializer(
            models.CustomUser.objects.get(id=current_user.id)
        )
        return Response(serializer.data)


class CreateTag(APIView):
    def post(self, request):
        interest = request.query_params.get('interest_name')
        print(f"likes {interest}")
        return Response(serializer.data)






