from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet

router = DefaultRouter()
router.register(r'warga', WargaViewSet)
router.register(r'pengaduan', PengaduanViewSet)

urlpatterns = router.urls
