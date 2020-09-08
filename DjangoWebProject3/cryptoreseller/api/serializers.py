from rest_framework import serializers
from ..models import Cryptoseller

class CryptoSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Cryptoseller
        fields =[
                "pk",
                "username",
                 "balance_amount",
                 "exchanger",
                 "Give",
                 "Get",
                 "Reserve",
                 "Reviews",
                 "Payment_method"
                 ]
        # read_only_fields = ['']
    # def validate_second_name(self, value):
    #     qs = Workers.objects.filter(title__iexact=value)
    #     if qs.exists():
    #