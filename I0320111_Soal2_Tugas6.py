print("Program Menghitung Nilai Rata-Rata")
banyak_data = int(input("Banyak data: "))
data = []
jumlah = 0
for x in range(0,banyak_data):
    temp = int(input("Masukkan data ke-%d: " % (x + 1)))
    data.append(temp)
    jumlah += data[x]
    rata_rata = jumlah/banyak_data
print("Nilai rata-ratanya adalah ", rata_rata)