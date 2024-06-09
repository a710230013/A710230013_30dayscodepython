class Kereta:
  def __init__(self, nama, kecepatan, warna):
    self.nama = nama
    self._kecepatan = kecepatan  
    self.warna = warna

  def set_kecepatan(self, kecepatan_baru):
    if kecepatan_baru >= 0:
      self._kecepatan = kecepatan_baru
    else:
      print(f"Kecepatan tidak boleh negatif! Kecepatan tetap {self._kecepatan}")

  def get_kecepatan(self):
    return self._kecepatan

  def __str__(self):
    return f"Kereta {self.nama} berwarna {self.warna} melaju dengan kecepatan {self._kecepatan} km/jam."

kereta_api = Kereta("Bima Sakti", 100, "Biru")

print(kereta_api)  

kereta_api.set_kecepatan(-50)  
kereta_api.set_kecepatan(150)

print(kereta_api)