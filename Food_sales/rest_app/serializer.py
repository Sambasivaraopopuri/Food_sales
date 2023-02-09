from rest_framework import serializers
from . models import *

class Serializers_Food_Sales(serializers.ModelSerializer):
    class Meta:
        model = Food_Sales
        fields = "__all__"