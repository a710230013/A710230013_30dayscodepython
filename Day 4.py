def hitung_luas_persegi(sisi):
  luas = sisi * sisi
  return luas

sisi = float(input("Masukkan sisi persegi: "))
luas = hitung_luas_persegi(sisi)
print(f"Luas persegi: {luas}")