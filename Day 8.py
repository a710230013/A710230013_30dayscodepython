def hitung_total_belanja(daftar_barang):
 
  total_belanja = 0
  for barang in daftar_barang:
    total_belanja += barang["harga"] * barang["jumlah"]
  return total_belanja

def main():
  daftar_barang = [
    {"nama": "Beras", "harga": 5000, "jumlah": 2},
    {"nama": "Gula", "harga": 7000, "jumlah": 1},
    {"nama": "Minyak Goreng", "harga": 10000, "jumlah": 2},
  ]

  total_belanja = hitung_total_belanja(daftar_barang)

  print("Daftar Belanja:")
  for barang in daftar_barang:
    print(f"- {barang['nama']} x {barang['jumlah']}: Rp{barang['harga']:,.2f}")
  print(f"Total Belanja: Rp{total_belanja:,.2f}")

if __name__ == "__main__":
  main()