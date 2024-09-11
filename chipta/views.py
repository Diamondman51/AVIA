from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from chipta.serializers import *
# Create your views here.


class ChiptaViewset(ModelViewSet):
    queryset = Chipta.objects.all()
    serializer_class = ChiptaSerializer
    pagination_class = PageNumberPagination


class YolovchiViewset(ModelViewSet):
    queryset = Yolovchi.objects.all()
    serializer_class = YolovchiSerializer
    pagination_class = PageNumberPagination


class Band_qilishViewset(ModelViewSet):
    queryset = Band_qilish.objects.all()
    serializer_class = Band_qilishSerializer
    pagination_class = PageNumberPagination

    def get_session_key(self):
        ...

    def create(self, request, *args, **kwargs):
        # For GET requests, use query_params instead of request.data
        print('----------------------------------------------------********************')
        print(request.data)  # This will print the query parameters
        print('----------------------------------------------------********************')
        return super().create(request, *args, **kwargs)


@api_view(["POST"])
def post(request):
    qayerdan = request.query_params.get('qayerdan')
    qayerga = request.query_params.get('qayerga')
    sanasi = request.query_params.get('sanasi')

    chipta = Chipta.objects.get(qaysi_shahardan=qayerdan, qaysi_shaharga=qayerga, ketish_vaqti=sanasi)

    ser = ChiptaSerializer(chipta)
    return Response(ser.data)
