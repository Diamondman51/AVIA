from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from chipta.models import *


class ChiptaSerializer(ModelSerializer):
    class Meta:
        model = Chipta
        fields = "__all__"

    def validate_raqam(self, value):
        print(type(value))
        if len(str(value)) != 10:
            raise serializers.ValidationError('Chipta raqami mos emas!!!')
        return value


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
        print('***********----------------')
        print(validated_data)
        print('***********----------------')
        chipta_data = validated_data.pop('chipta')
        yolovchi_data = validated_data.pop('yolovchi')

        chipta = Chipta.objects.get(raqam=chipta_data['raqam'])

        yolovchi = Yolovchi.objects.get(ismi=yolovchi_data['ismi'])

        if chipta.soni > 0:
            band_qilish = Band_qilish.objects.create(chipta=chipta, yolovchi=yolovchi)
            chipta.soni -= 1
            chipta.save()
        else:
            chipta.delete()
            raise serializers.ValidationError('Bilet tugagan')

        return band_qilish

    # def validate_raqam(self, attrs):
    #     ...

    # def list(self, request, *args, **kwargs):
    #     # For GET requests, use query_params instead of request.data
    #     print(request.data)  # This will print the query parameters
    #     return super().list(request, *args, **kwargs)

