from models import Mobil, Motor, Dealer, Pelanggan
from services import BeliService, JualService

# DealerMaju
# 4
# mobil M001 Avanza 2020 Toyota bensin ya 200000000 7
# mobil M002 Brio 2022 Honda bensin tidak 180000000 5
# motor T001 Vario 2021 Honda bensin ya 20000000
# mobil M001 Xenia 2019 Daihatsu bensin ya 150000000 7
# 3
# Andi 08777666 3 M002
# Budi 08123456 1 M001,T001
# Sari 08999888 2 M001

pilihan = {'mobil': Mobil, 'motor': Motor}
dealer = Dealer(input())
beli = BeliService(dealer)
jual = JualService(dealer)

n = int(input())
cadangan = None
for _ in range(n):
    bagian = input().split()
    jenis, kode, seri, tahun, brand, bbm, bekas, harga = bagian[:8]
    args = [kode, seri, int(tahun), brand, bbm, bekas , int(harga)]
    if jenis == 'mobil':
        args.append(int(bagian[8]))
    kendaraan = pilihan[jenis](*args)
    cadangan = cadangan or kendaraan
    try:
        beli.beli_kendaraan(kendaraan)
        print('Beli OK:', kendaraan.kode)
    except (TypeError, ValueError) as e:
        print('Beli Gagal:', e)

print('Stok Setelah Beli:', dealer.total_kendaraan())

# kasus error pembelian
for nama, objek in [('Duplikat', cadangan), ('Bukan Kendaraan', 'sepeda'), ('Harga Negatif', Motor('X1', 'S', 2020, 'B', 'bensin', False, -5))]:
    try:
        beli.beli_kendaraan(objek)
        print(f'Beli {nama}: berhasil (tidak diharapkan)')
    except (TypeError, ValueError) as e:
        print(f'Beli {nama}:', type(e).__name__, '-', e)

# kasus error pencarian
print('Cari Ada:', beli.cari_kendaraan(cadangan.kode) is cadangan if cadangan else None)
print('Cari Tidak Ada:', beli.cari_kendaraan('TIDAK-ADA'))

# kasus error penjualan
stok_kini = [k.kode for k in dealer.stok]
kode_ada = stok_kini[0] if stok_kini else 'X'
kasus = [
    ('Bukan Pelanggan', ('budi', [kode_ada], 1)),
    ('Tanggal Bukan Int', (Pelanggan('Budi', '08123'), [kode_ada], '2026-01-01')),
    ('Daftar Kosong', (Pelanggan('Budi', '08123'), [], 1)),
    ('Kode Double', (Pelanggan('Budi', '08123'), [kode_ada, kode_ada], 1)),
    ('Kode Tidak Ada', (Pelanggan('Budi', '08123'), ['TIDAK-ADA'], 1)),
]
for nama_kasus, args in kasus:
    try:
        jual.jual_kendaraan(*args)
        print(f'Jual {nama_kasus}: berhasil (tidak diharapkan)')
    except (TypeError, ValueError) as e:
        print(f'Jual {nama_kasus}:', type(e).__name__, '-', e)

print('Stok Akhir:', stok_kini == [k.kode for k in dealer.stok], len(dealer.stok))
print('Riwayat:', len(jual.riwayat))
print('Total Pendapatan:', jual.total_pendapatan())
print('Kendaraan Terjual Hilang Dari Stok:', all(beli.cari_kendaraan(i.kendaraan.kode) is None for t in jual.riwayat for i in t.daftar_item))

# UJI JUAL
m = int(input())
for _ in range(m):
    nama, kontak, tanggal, kodes = input().split()
    daftar = kodes.split(',')
    try:
        trx = jual.jual_kendaraan(Pelanggan(nama, kontak), daftar, int(tanggal))
        print('Jual OK:', trx.kode, 'Item:', len(trx.daftar_item), 'Total:', trx.total_harga())
    except (TypeError, ValueError) as e:
        print("error")
        print('Jual Gagal:', e)
    print('Stok:', dealer.total_kendaraan())

