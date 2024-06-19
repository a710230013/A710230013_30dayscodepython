try:
    num1 = int(input("Masukkan angka pertama: "))
    num2 = int(input("Masukkan angka kedua: "))
    hasil = num1 / num2
    print(f"Hasil pembagian: {hasil}")
except ValueError:
    print("Input harus berupa angka!")
except ZeroDivisionError:
    print("Tidak bisa melakukan pembagian dengan nol!")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
finally:
    print("Program selesai.")