from rest_framework import serializers
from .models import Box
class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ['id', 'nome', 'numero']
        # quero usar todos os campos
        # fields = '__all__'