from rest_framework import serializers
from .models import new

class EmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = new
        fields = '__all__' 