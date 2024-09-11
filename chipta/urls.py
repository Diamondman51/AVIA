from django.urls import path
from rest_framework.routers import DefaultRouter

from chipta.views import *

router = DefaultRouter()
router.register("chipta", ChiptaViewset, 'chipta')
router.register("yolovchi", YolovchiViewset, 'Yolovchi')
router.register("band_qilish", Band_qilishViewset, 'Band_qilish')


urlpatterns = router.urls + [
    path('pp/', post)
]