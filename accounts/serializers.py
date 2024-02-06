from rest_framework import serializers
from accounts.models import User,Realtor,Vote
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('full_name','password','phone_number','code',)

    def validate_password(self, value):
        """
        Hash value passed by user.
        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

class RealtorSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    class Meta:
        model= Realtor
        fields =('id','user','address','rate','description','stars_average')

class VoteSerializer(serializers.Serializer):
    realtor = serializers.CharField(required=True)
    vote = serializers.IntegerField(required=True,max_value=5,min_value=0)
