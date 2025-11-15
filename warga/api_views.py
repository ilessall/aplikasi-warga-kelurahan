from rest_framework import generics
from .models import Warga, Pengaduan
from .serializers import WargaSerializer, PengaduanSerializer

class WargaListCreateAPI(generics.ListCreateAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class WargaDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer


class PengaduanListCreateAPI(generics.ListCreateAPIView):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer

class PengaduanDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer
