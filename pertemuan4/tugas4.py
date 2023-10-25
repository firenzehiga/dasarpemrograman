# TUGAS NO.1
nama = "Firenze Higa Putra"
umur = 19

if(umur >= 1 and umur <= 18):
    keterangan = "Anak-Anak"
elif(umur >= 18 and umur <= 65):
    keterangan = "Dewasa"
elif(umur >= 65 and umur <=100 ):
    keterangan = "Lanjut Usia"
else:
    keterangan = "Ras Elf inimah"

print("Nama \t:", nama, 
    "\nUmur \t\t:",umur, 
    "\nKeterangan \t:", keterangan) 
print()


# TUGAS NO.2
angka1 = 30
angka2 = 20

if(angka1 > angka2):
    keterangan = "Angka Pertama lebih besar dari Angka Kedua"
elif(angka1 < angka2):
    keterangan = "Angka Pertama lebih kecil dari Angka Kedua"
elif(angka1 == angka2):
    keterangan = "Angka Pertama sama dengan Angka Kedua"
else:
    keterangan = "Terjadi Kesalahan"

print("Angka Pertama \t:", angka1, 
    "\nAngka Kedua \t:",angka2, 
    "\nKeterangan \t:", keterangan) 
