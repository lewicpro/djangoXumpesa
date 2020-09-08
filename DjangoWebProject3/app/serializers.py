from rest_framework import serializers
from.models import UserInfo


class AppSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = 'id','full_name', 'amount','Phone_no'
