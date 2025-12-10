from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Warga, Pengaduan
from .serializers import WargaSerializer, PengaduanSerializer


class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer
    permission_classes = [IsAdminUser]
