from rest_framework import viewsets
from .models import Warga, Pengaduan
from .serializers import WargaSerializer, PengaduanSerializer

# ======================
# API VIEWSETS (PERTEMUAN 7)
# ======================

class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer


class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer
