#menghitung rata rata

banyakdata = int(input("Bantak data yang akan dihitung: "))
data = []
jumlah = 0

for i in range(0, banyakdata):
    nilaidata = int(input("Masukkan nilai data ke-%d: " % (i+1)))
    data.append(nilaidata)
    i+=1

for item in data:
    jumlah += item


ratarata = jumlah / banyakdata
print("Rata-Rata: ", round(ratarata,2))