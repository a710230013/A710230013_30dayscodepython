buah = {
    "Apel": 3000,
    "Pisang": 5000,
    "Jeruk": 8000,
    "Mangga": 10000,
    "Anggur": 15000,
}

def display_buah():
    print("\nDaftar Buah dan Harga:")
    for nama, harga in buah.items():
        print(f"{nama}: Rp{harga}")

def add_buah():
    nama_baru = input("Masukkan nama buah baru: ")
    harga_baru = int(input(f"Masukkan harga {nama_baru}: "))
    buah[nama_baru] = harga_baru
    print(f"Buah {nama_baru} telah ditambahkan dengan harga Rp{harga_baru}.")

def delete_buah():
    nama_hapus = input("Masukkan nama buah yang ingin dihapus: ")
    if nama_hapus in buah:
        del buah[nama_hapus]
        print(f"Buah {nama_hapus} telah dihapus.")
    else:
        print(f"Buah {nama_hapus} tidak ditemukan.")

def search_buah():
    nama_cari = input("Masukkan nama buah yang ingin dicari: ")
    if nama_cari in buah:
        harga = buah[nama_cari]
        print(f"Harga {nama_cari} adalah Rp{harga}.")
    else:
        print(f"Buah {nama_cari} tidak ditemukan.")

def transaksi():
    while True:
        display_buah()

        nama_beli = input("Masukkan nama buah yang ingin dibeli: ")
        if nama_beli in buah:
            jumlah_beli = int(input(f"Masukkan jumlah {nama_beli} yang ingin dibeli: "))
            harga = buah[nama_beli]
            total_harga = jumlah_beli * harga

            print(f"\nDetail Transaksi:")
            print(f"{nama_beli} x {jumlah_beli} = Rp{total_harga}")

            bayar = int(input("Masukkan uang pembayaran: "))
            kembalian = bayar - total_harga

            if bayar >= total_harga:
                print(f"Uang pembayaran cukup. Kembalian: Rp{kembalian}")
                break
            else:
                print(f"Uang pembayaran tidak cukup. Transaksi dibatalkan.")
        else:
            print(f"Buah {nama_beli} tidak ditemukan.")

while True:
    print("\nMenu Toko Buah:")
    print("1. Tampilkan Daftar Buah")
    print("2. Tambah Buah Baru")
    print("3. Hapus Buah")
    print("4. Cari Buah")
    print("5. Transaksi")
    print("6. Keluar")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        display_buah()
    elif pilihan == "2":
        add_buah()
    elif pilihan == "3":
        delete_buah()
    elif pilihan == "4":
        search_buah()
    elif pilihan == "5":
        transaksi()
    elif pilihan == "6":
        break
    else:
        print("Pilihan tidak valid.")
