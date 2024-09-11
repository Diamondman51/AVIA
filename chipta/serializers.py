from dataclasses import fields
from pyexpat import model

from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from chipta.models import *


class ChiptaSerializer(ModelSerializer):
    class Meta:
        model = Chipta
        fields = "__all__"


class YolovchiSerializer(ModelSerializer):
    class Meta:
        model = Yolovchi
        fields = "__all__"


class ChiptaSerializer2(ModelSerializer):
    class Meta:
        model = Chipta
        fields = ["raqam"]


class YolovchiSerializer2(ModelSerializer):
    class Meta:
        model = Yolovchi
        fields = ["ismi"]


class Band_qilishSerializer(ModelSerializer):
    yolovchi = YolovchiSerializer2()
    chipta = ChiptaSerializer2()

    class Meta:
        model = Band_qilish
        fields = ["yolovchi", 'chipta']

    def create(self, validated_data):
        # Extract nested data for chipta and yolovchi
        print('***********----------------')
        print(validated_data)
        print('***********----------------')
        chipta_data = validated_data.pop('chipta')
        yolovchi_data = validated_data.pop('yolovchi')

        # Retrieve or create Chipta instance based on 'raqam'
        chipta = Chipta.objects.get(raqam=chipta_data['raqam'])

        # Retrieve or create Yolovchi instance based on 'ismi'
        yolovchi = Yolovchi.objects.get(ismi=yolovchi_data['ismi'])

        # Create Band_qilish instance with the related objects
        band_qilish = Band_qilish.objects.create(chipta=chipta, yolovchi=yolovchi)
        return band_qilish

    # def validate_raqam(self, attrs):
    #     ...

    # def list(self, request, *args, **kwargs):
    #     # For GET requests, use query_params instead of request.data
    #     print(request.data)  # This will print the query parameters
    #     return super().list(request, *args, **kwargs)

