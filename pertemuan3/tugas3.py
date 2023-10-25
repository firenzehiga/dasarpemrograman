print('< Program Data Diri >')
print('====================================')
print()

# Biodata Diri
nama = "Firenze Higa Putra"
nim  = "0110223014"
kelas = "TI01"
no_telp =  "085894310722"
almt = "Mutiara Venezia Residence Cileungsi"

print("Nama :" , nama,'\n' 
        "NIM :" , nim,'\n' 
        "Kelas :" , kelas,'\n' 
        "No. Telp :" , no_telp,'\n' 
        "Alamat : " , almt, '\n')

# Biodata Teman
nama = "Nicky Fajaelani"
nim  = "110223044"
kelas = "TI01"
no_telp =  "085700957991"
almt = "Bogor"

print("Nama :" , nama,'\n' 
        "NIM :" , nim,'\n' 
        "Kelas :" , kelas,'\n' 
        "No. Telp :" , no_telp,'\n' 
        "Alamat :" , almt, '\n')


# Mencari Berat Badan Ideal
print('< Program Mencari Berat Badan Ideal  >')
print('====================================')
print()

tinggi_badan = 175
berat_ideal = (tinggi_badan - 100) - ((tinggi_badan - 100) * 10/100)

print("Berat Badan idealnya adalah", berat_ideal, '\n')
	
# Mencari nilai konveri suhu Celcius ke Farenheit 	
print('< Program Konversi Suhu Celcius ke Fahrenheit >')
print('===============================================')
print()

celcius = 60
fahrenheit = (9/5 * celcius) + 32

print(int(celcius),"derajat Celsius =",int(fahrenheit)  ,"derajat Fahrenheit",'\n')



print("< Program Python Hitung Luas & Keliling Tabung > ")

phi    = 3.14
jari   = 10
tinggi = 20
luas   = 2*phi*jari*(jari+tinggi)
keliling = 2*phi*jari

print("Luas Permukaan Tabung =",int(luas)) 
print("Keliling Tabung       =",int(keliling))
