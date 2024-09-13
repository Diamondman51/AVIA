import pprint

from rest_framework import serializers
from chipta.models import Chipta, Yolovchi, Band_qilish


class ChiptaSer(serializers.ModelSerializer):
    class Meta:
        model = Chipta
        fields = ["raqam", 'kompaniya', 'qaysi_shaharga', 'qaysi_shahardan']
        # extra_kwargs = {
        #     'raqam': {'validators': []},  # Disable the unique validation
        # }

    # Instead of creating, we just validate the raqam
    def to_internal_value(self, data):
        try:
            print(999999999999999999999999999999999)
            print(data)
            d = {key: value for key, value in data.items()}
            pprint.pprint(d)
            print()
            # chipta = Chipta.objects.get(**{key: value for key, value in data.items()})
            chipta = Chipta.objects.get(raqam=data.get('raqam'))
            return chipta
        except Chipta.DoesNotExist:
            raise serializers.ValidationError({'raqam': f'Chipta with this raqam does not exist: {data.get("raqam")}'})


class YolovchiSer(serializers.ModelSerializer):
    class Meta:
        model = Yolovchi
        fields = "__all__"

    def to_internal_value(self, data):
        try:
            # Try to get the existing Yolovchi by ismi
            # print(777777777777777777777777777777777777)
            print(data)
            yolovchi = Yolovchi.objects.get(**{key: value for key, value in data.items()})
            return yolovchi
        except Yolovchi.DoesNotExist:
            # Print the data for debugging

            print(data)
            # Create a new Yolovchi using the data passed
            yolovchi = Yolovchi.objects.create(**{key: value for key, value in data.items()})
            print(5555555555555555555555555)
            print(yolovchi)
            return yolovchi

            # raise serializers.ValidationError({'ismi': 'Yolovchi with this ismi does not exist.'})


class Band_qilishSer(serializers.ModelSerializer):
    yolovchi = YolovchiSer()
    chipta = ChiptaSer()

    class Meta:
        model = Band_qilish
        fields = ['id', 'chipta', 'yolovchi']

    def create(self, validated_data):
        print(validated_data)
        # Fetch existing Chipta
        chipta = validated_data.get('chipta') # this is object

        # Fetch or create Yolovchi (depending on your requirements)
        # yolovchi = validated_data.get('yolovchi')
        # Create Band_qilish instance
        band = Band_qilish.objects.create(**validated_data)
        chipta.is_reserved = True
        chipta.save()
        return band
