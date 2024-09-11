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


class Band_qilishSerializer(ModelSerializer):
    class Meta:
        model = Band_qilish
        fields = "__all__"

    # def list(self, request, *args, **kwargs):
    #     # For GET requests, use query_params instead of request.data
    #     print(request.data)  # This will print the query parameters
    #     return super().list(request, *args, **kwargs)
