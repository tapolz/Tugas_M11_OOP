from .kendaraan import Kendaraan

class Mobil(Kendaraan):
  pajak = 0.5

  def __init__(self, kode, seri, tahun, brand, tipe_bahan_bakar, status_bekas, harga, jumlah_kursi):
    super().__init__(kode, seri, tahun, brand, tipe_bahan_bakar, status_bekas, harga)
    self.jumlah_kursi = jumlah_kursi

  def info(self):
    return f"Mobil | {super().info()} | Jumlah kursi: {self.jumlah_kursi}"

  def harga_jual(self):
    potongan_harga = 0

    if self.status_bekas:
        potongan_harga = 0.3

    return self.harga * potongan_harga / self.pajak