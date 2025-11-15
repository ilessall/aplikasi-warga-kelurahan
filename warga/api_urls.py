from django.urls import path
from .views import WargaListAPIView, WargaDetailAPI

urlpatterns = [
    path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    path('warga/<int:pk>/', WargaDetailAPI.as_view(), name='api-warga-detail'),
]
