from .kendaraan import Kendaraan

class Motor(Kendaraan):
  pajak = 0.2

  def info(self):
    return f"Motor | {super().info()}"

  def harga_jual(self):
    potongan_harga = 0

    if self.status_bekas:
        potongan_harga = 0.4

    return self.harga * potongan_harga / self.pajak

