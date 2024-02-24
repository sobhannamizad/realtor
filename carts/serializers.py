from rest_framework import serializers
from carts.models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['users'] = instance.user.full_name
        data['property'] = instance.property.title
        return data