from rest_framework import serializers
from .models import LogisticsBox, Exception, ProductBox

class ExceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exception
        fields = ['serial_number', 'details', 'logistics_box', 'flag']

class LogisticsBoxSerializer(serializers.ModelSerializer):
    exceptions = ExceptionSerializer(many=True, read_only=True)
    
    class Meta:
        model = LogisticsBox
        fields = ['logistics_box_id', 'details', 'flag', 'exceptions']

class ProductBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBox
        fields = [
            'logistics_box_id', 'logistics_box_timestamp', 'number_units',
            'article_number', 'product_box_id', 'product_serial',
            'device_creation_timestamp', 'device_remarks'
        ]
