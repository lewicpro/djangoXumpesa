from rest_framework import serializers
from.models import Products


class MarketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            'id',
            'username',
            'category',
            'country',
            'stock_products',
            'title',
            'currency',
            'color',
            'image',
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'description',
            'updated',
            'Price_sold',
            'timestamp',
            'condition',
            'Receive_acc',
            'Price',
            'currency'
        ]

