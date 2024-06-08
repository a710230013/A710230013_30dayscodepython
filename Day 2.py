def main():

  while True:
    print("\nKalkulator Sederhana")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("0. Keluar")

    pilihan = input("Pilih operasi (1/2/3/4/0): ")

    if pilihan == "0":
      break

    try:
      bilangan1 = float(input("Masukkan bilangan pertama: "))
      bilangan2 = float(input("Masukkan bilangan kedua: "))
    except ValueError:
      print("Input tidak valid! Masukkan angka desimal.")
      continue

    if pilihan == "1":
      hasil = bilangan1 + bilangan2
      operasi = "+"
    elif pilihan == "2":
      hasil = bilangan1 - bilangan2
      operasi = "-"
    elif pilihan == "3":
      hasil = bilangan1 * bilangan2
      operasi = "*"
    elif pilihan == "4":
      if bilangan2 == 0:
        print("Pembagian dengan nol tidak diizinkan!")
        continue
      hasil = bilangan1 / bilangan2
      operasi = "/"
    else:
      print("Pilihan tidak valid!")
      continue

    print(f"{bilangan1} {operasi} {bilangan2} = {hasil}")

if __name__ == "__main__":
  main()