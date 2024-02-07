from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    id= serializers.CharField(read_only=True)
    owner= serializers.CharField(read_only=True)
    class Meta:
        model = Property
        fields =('id','image','price','prepayment','title','description','address','type','owner')
