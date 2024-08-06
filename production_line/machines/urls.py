from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'logisticsboxes', views.LogisticsBoxViewSet)
router.register(r'exceptions', views.ExceptionViewSet)
router.register(r'productboxes', views.ProductBoxViewSet)

urlpatterns = [
    path('update/<str:machine_name>/', views.machine_update, name='machine_update'),
    path('', include(router.urls)),
    path('logisticsboxes/<int:box_id>/exceptions/', views.exceptions_for_box, name='exceptions_for_box'),
    path('logisticsboxes/<int:box_id>/', views.get_logistics_box, name='get_logistics_box'),
]
