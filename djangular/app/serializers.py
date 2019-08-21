from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Singer

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id', 'first_name', 'last_name', 'style']
