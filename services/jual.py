from models import Dealer, Pelanggan, Transaksi, ItemTransaksi
from utils.validation import valid_kode, valid_jumlah

class JualService:
  def __init__(self, dealer: Dealer):
    self.dealer = dealer
    self.riwayat = []

  def cari_kendaraan(self, kode):
    return next((k for k in self.dealer.stok if k.kode == kode), None)

  def jual_kendaraan(self, pelanggan: Pelanggan, daftar_kode, tanggal: int):
    if not isinstance(pelanggan, Pelanggan):
      raise TypeError("pembeli harus berupa objek Pelanggan")
    if not isinstance(tanggal, int):
      raise ValueError("tanggal harus berupa int (bilangan bulat)")
    if not daftar_kode:
      raise ValueError("pilih minimal satu kendaraan")
    if len(set(daftar_kode)) != len(daftar_kode):
      raise ValueError("ada kode kendaraan yang double")

    terpilih = []  
    for kode in daftar_kode:
      if not valid_kode(kode):
        raise ValueError(f"kode tidak valid: {kode}")
      kendaraan = self.cari_kendaraan(kode)
      if kendaraan is None:
        raise ValueError(f"kendaraan {kode} tidak ada di stok {self.dealer.nama}")
      terpilih.append(kendaraan)

    transaksi = Transaksi(f"TRX-{len(self.riwayat) + 1:03d}", tanggal, pelanggan, self.dealer)
    for kendaraan in terpilih:
      jumlah = 1  
      if not valid_jumlah(jumlah):
        raise ValueError("jumlah tidak valid")
      transaksi.tambah_item(ItemTransaksi(kendaraan, jumlah))

    for kendaraan in terpilih:
      self.dealer.stok.remove(kendaraan)

    self.riwayat.append(transaksi)
    return transaksi

  def total_pendapatan(self):
    return sum(t.total_harga() for t in self.riwayat)
