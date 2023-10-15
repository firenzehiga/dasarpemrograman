berat_badan = int(input('Masukan Berat Badan (kg) : '))
tinggi_badan = int(input('Masukan Tinggi Badan (cm) : '))

berat_ideal = (tinggi_badan - 100) - ((tinggi_badan - 100) * 10/100)
print(berat_ideal)
