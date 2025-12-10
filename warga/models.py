from django.db import models

class Warga(models.Model):
    nik = models.CharField(max_length=20, unique=True)
    nama_lengkap = models.CharField(max_length=100)
    alamat = models.TextField()
    no_telepon = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_lengkap


class Pengaduan(models.Model):
    pelapor = models.ForeignKey(Warga, on_delete=models.CASCADE, related_name='pengaduan')
    judul = models.CharField(max_length=150)
    deskripsi = models.TextField()
    status = models.CharField(max_length=50, default='Menunggu')
    tanggal_lapor = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
