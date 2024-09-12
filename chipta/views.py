from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from chipta.models import Chipta, Yolovchi, Band_qilish
from chipta.serializers import ChiptaSerializer, YolovchiSerializer, Band_qilishSerializer


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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_session_key(self):
        ...

    def list(self, request, *args, **kwargs):
        print('list, data', request.data)
        print('list, params', request.query_params)
        print('list, get', request.GET)
        return super().list(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     # For GET requests, use query_params instead of request.data
    #     print('----------------------------------------------------********************')
    #     print('params', request.query_params)  # This will print the query parameters
    #     print('data', request.data)  # This will print the query parameters
    #     print('----------------------------------------------------********************')
    #     return super().create(request, *args, **kwargs)


@api_view(["POST"])
def post(request):
    qayerdan = request.query_params.get('qayerdan')
    qayerga = request.query_params.get('qayerga')
    sanasi = request.query_params.get('sanasi')

    chipta = Chipta.objects.get(qaysi_shahardan=qayerdan, qaysi_shaharga=qayerga, ketish_vaqti=sanasi)

    ser = ChiptaSerializer(chipta)
    return Response(ser.data)
