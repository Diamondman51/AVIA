from django.urls import path
from rest_framework.routers import DefaultRouter

from chipta.views import *

router = DefaultRouter()
router.register("flights", ChiptaViewset, 'flights')
router.register("passengers", YolovchiViewset, 'passengers')
router.register("reservations", Band_qilishViewset, 'reservations')
# router.register("user", UserViewset, 'user')


urlpatterns = router.urls + [
    path("findflights/", post),
]
