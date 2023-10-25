
customer = "Budi Santoso"
totalBelanja= 150000

if(totalBelanja > 100000):
    keterangan = "Selamat Anda mendapat Hadiah"
else:
    keterangan = "Terima Kasih sudah berbelanja"

print("Customer", customer, "\nTotal Belanja Anda Rp.", totalBelanja, "\n",keterangan)
print()

# Struktur Kendali - Ternary(2)

# Siswa dinyatakan lulus minimal 60 nilainya
nama = "Firenze Higa Putra"
matpel = "Matematika"
nilai = 79.99
# ternary
keterangan = "Lulus" if nilai >= 60 else "Gagal"

#cetak
print("Nama Siswa \t:", nama, 
    "\nMata Pelajaran \t:", matpel, 
    "\nNilai \t\t:",nilai, 
    "\nKeterangan \t:", keterangan)
print()


# if multi kondisi 
nama = "Firenze Higa Putra"
matpel = "Matematika"
nilai - 80

# uji grade dengan IF Multi Kondisi
if(nilai>= 85 and nilai <=100):
    grade = "A"
elif(nilai>= 75 and nilai <=85):
    grade = "B"
elif(nilai>= 60 and nilai <=75):
    grade = "C"
elif(nilai>= 30 and nilai <=60):
    grade = "D"
else:
    grade = "E"

print("Nama Siswa \t:", nama, 
    "\nMata Pelajaran \t:", matpel, 
    "\nNilai \t\t:",nilai, 
    "\nGrade \t:", grade) 