from .kendaraan import Kendaraan

class Transaksi:
  def __init__(self, kode, tanggal, pelanggan, dealer, daftar_item=None):
    self.kode = kode
    self.tanggal = tanggal
    self.pelanggan = pelanggan
    self.dealer = dealer
    self.daftar_item = list(daftar_item or [])

  def info(self):
    detail_item = "\n".join(item.info() for item in self.daftar_item)
    return f"Transaksi: {self.kode} | Tanggal: {self.tanggal} | Pelanggan: {self.pelanggan.nama} | Dealer: {self.dealer.nama} | Total: Rp{self.total_harga():,}\n{detail_item}"

  def total_harga(self):
    return sum(item.subtotal() for item in self.daftar_item)

  def tambah_item(self, item):
    self.daftar_item.append(item)