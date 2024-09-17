from rest_framework import serializers
from api import models

class Authors(serializers.ModelSerializer):
    class Meta:
        model = models.Authors
        fields = '__all__'