from django.urls import path,include
from .views import BoxViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('boxes',BoxViewSet,basename='box')
urlpatterns = [
    path('', include(router.urls)),
]






"""
from django.urls import path
from apibox_app.views import box

urlpatterns = [
    path('box/', box, name='box'),
]


"""
