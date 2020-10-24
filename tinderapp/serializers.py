from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username','available','interests', 'id', 'description')

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Interest
        fields = ('name', )
