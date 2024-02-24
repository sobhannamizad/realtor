from rest_framework import serializers
from django.core.exceptions import ValidationError


class BalanceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    amount = serializers.IntegerField()

    def validate_amount(self, value):
        if value < 0 :
            raise ValidationError('amount cant be zero')
        return value