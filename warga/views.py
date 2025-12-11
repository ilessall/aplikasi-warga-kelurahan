from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Warga, Pengaduan
from .serializers import WargaSerializer, PengaduanSerializer


class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-id')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Tambahan Searching + Ordering
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'id']


class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all().order_by('-id')
    serializer_class = PengaduanSerializer
    permission_classes = [IsAdminUser]

    # Tambahan Searching + Ordering
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['judul', 'deskripsi']
    ordering_fields = ['status', 'id']
