from models import Dealer, Kendaraan
from utils.validation import valid_kode, valid_harga

class BeliService:
  def __init__(self, dealer: Dealer):
    self.dealer = dealer

  def cari_kendaraan(self, kode):
    return next((k for k in self.dealer.stok if k.kode == kode), None)

  def beli_kendaraan(self, kendaraan: Kendaraan):
    if not isinstance(kendaraan, Kendaraan):
      raise TypeError("yang dibeli harus berupa objek Kendaraan (Mobil/Motor)")
    if not valid_kode(kendaraan.kode):
      raise ValueError(f"kode tidak valid: {kendaraan.kode}")
    if not valid_harga(kendaraan.harga):
      raise ValueError(f"harga tidak valid: {kendaraan.harga}")
    if self.cari_kendaraan(kendaraan.kode) is not None:
      raise ValueError(f"kode kendaraan sudah ada di stok: {kendaraan.kode}")

    self.dealer.tambah_kendaraan(kendaraan)
    return kendaraan
