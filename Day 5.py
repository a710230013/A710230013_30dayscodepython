def hitung_gaji(nama, gaji_pokok, jam_kerja, tunjangan_anak=0):
  
  if jam_kerja > 40:
    lembur = jam_kerja - 40
    gaji_lembur = lembur * 1.5 * gaji_pokok
  else:
    lembur = 0
    gaji_lembur = 0

  total_gaji = gaji_pokok * jam_kerja + gaji_lembur + tunjangan_anak

  print(f"Nama: {nama}")
  print(f"Gaji Pokok: Rp{gaji_pokok:,}")
  print(f"Jam Kerja: {jam_kerja} jam")
  print(f"Lembur: {lembur} jam")
  print(f"Gaji Lembur: Rp{gaji_lembur:,}")
  print(f"Tunjangan Anak: Rp{tunjangan_anak:,}")
  print(f"Total Gaji: Rp{total_gaji:,}")

nama = input("Masukkan nama karyawan: ")
gaji_pokok = int(input("Masukkan gaji pokok per jam: "))
jam_kerja = int(input("Masukkan jumlah jam kerja: "))
tunjangan_anak = int(input("Masukkan jumlah tunjangan anak (opsional): "))

hitung_gaji(nama, gaji_pokok, jam_kerja, tunjangan_anak)