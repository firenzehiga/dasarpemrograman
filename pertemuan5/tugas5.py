
# Latihan No 1

print('< Program Operasi pada List Kendaraan  >')
print('====================================')

vehicleList = ["YZF R1", "Sport", 988, "Merah", 2]
vehicleList.append("308 Juta") 
vehicleList.append("Premium")
vehicleList.insert(2, "Yamaha")

print("Nama  :",vehicleList[0],
    "\nJenis :",vehicleList[1],
    "\nMerk  :",vehicleList[2],
    "\nCC    :",vehicleList[3],
    "\nWarna :",vehicleList[4],
    "\nRoda  :",vehicleList[5],
    "\nHarga :",vehicleList[6],
    "\nTipe  :",vehicleList[7],)
print()


print('< Program Match Case Bangun Datar  >')
print('====================================')

pilihan = int(input("Pilih Bangun Datar (1: persegi, 2: lingkaran, 3: segitiga): "))

# Latihan o 2
match pilihan:
        case 1:
            sisi = float(input("Masukkan sisi persegi: "))
            l_persegi = sisi ** 2
            print("Luas persegi:", int(l_persegi))
        case 2:
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            l_lingkaran = 3.14 * jari_jari ** 2
            print("Luas lingkaran:", int(l_lingkaran))
        case 3:
            alas = float(input("Masukkan alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            l_segitiga = 0.5 * alas * tinggi
            print("Luas segitiga:", int(l_segitiga))
        case _:
            print("Pilihan tidak tersedia")









