from rest_framework import serializers
from ..models import Profile

class dpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_photo', ]