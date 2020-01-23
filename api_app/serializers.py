from rest_framework import serializers
from .models import Profile

class walletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['balance', ]