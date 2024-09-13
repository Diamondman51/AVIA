from django.urls import path
from rest_framework.routers import DefaultRouter

from chipta.views import ChiptaViewset, BandQilishViewset, YolovchiViewset, chipta

router = DefaultRouter()
router.register('flights', ChiptaViewset, 'chipta')
router.register('passengers', YolovchiViewset, 'yolovchi')
router.register('reservations', BandQilishViewset, 'bandqilish')

urlpatterns = router.urls + [
    path('chipta/', chipta, name='chipta')
]
