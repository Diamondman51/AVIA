from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from chipta.models import Chipta, Yolovchi, Band_qilish
from chipta.serializers import ChiptaSer, YolovchiSer, Band_qilishSer


class ChiptaViewset(ModelViewSet):
    queryset = Chipta.objects.all()
    serializer_class = ChiptaSer
    pagination_class = PageNumberPagination


class YolovchiViewset(ModelViewSet):
    queryset = Yolovchi.objects.all()
    serializer_class = YolovchiSer
    pagination_class = PageNumberPagination


class BandQilishViewset(ModelViewSet):
    queryset = Band_qilish.objects.all()
    serializer_class = Band_qilishSer
    pagination_class = PageNumberPagination


@api_view(['POST'])
def chipta(request):
    # if request.method == 'POST':
    req = None
    qayerdan = request.query_params.get('qayerdan')
    qayerga = request.query_params.get('qayerga')
    sanasi = request.query_params.get('sanasi')
    dict_ = {}
    if qayerdan:
        dict_['qaysi_shahardan'] = qayerdan
    if qayerga:
        dict_['qaysi_shaharga'] = qayerga
    if sanasi:
        dict_['ketish_vaqti'] = sanasi

    if dict_:
        print(dict_)
        data = Chipta.objects.filter(**dict_)
    else:
        data = Chipta.objects.all()
    ser = ChiptaSer(data, many=True)
    return Response(ser.data)
