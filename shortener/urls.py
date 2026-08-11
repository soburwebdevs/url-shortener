from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shortener import views


router = DefaultRouter()
router.register('', views.LinkViewSet, basename='link')

urlpatterns = [
    path('', include(router.urls)),
]



