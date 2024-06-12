import smtplib
from email.mime.text import MIMEText

pengirim = "pengirim@example.com"
kata_sandi = "passwordpengirim"
penerima = "penerima@example.com"
judul = "Judul Email"
isi_email = "Isi email yang ingin Anda kirimkan."

pesan = MIMEText(isi_email)
pesan['From'] = pengirim
pesan['To'] = penerima
pesan['Subject'] = judul

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login(pengirim, kata_sandi)

    smtp.sendmail(pengirim, penerima, pesan.as_string())

print("Email terkirim!")