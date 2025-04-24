from rest_framework import serializers
from core.models import Cor

class CorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cor
        fields = '__all__'