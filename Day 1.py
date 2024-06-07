class Kendaraan:
  
  def __init__(self, merek, model, tahun):
    self.merek = merek
    self.model = model
    self.tahun = tahun

  def nyalakan(self):
    print("Mesin menyala...")

class Mobil(Kendaraan):
 
  def __init__(self, merek, model, tahun, jumlah_pintu):
    super().__init__(merek, model, tahun) 
    self.jumlah_pintu = jumlah_pintu

  def kendarai(self):
    print("Mengemudi mobil...")

kendaraan = Kendaraan("Tesla", "Model S", 2023)

mobil = Mobil("Honda", "Civic", 2020, 4)

print(kendaraan.merek)  
print(mobil.model)  

kendaraan.nyalakan()  
mobil.kendarai() 