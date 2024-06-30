class Mobil:
  def move(self):
    print("Berjalan di jalan raya")

class Pesawat:
  def move(self):
    print("Terbang di udara")

class Kapal:
  def move(self):
    print("Berlayar di laut")

mobil = Mobil()
pesawat = Pesawat()
kapal = Kapal()

pesawat.move()
kapal.move()