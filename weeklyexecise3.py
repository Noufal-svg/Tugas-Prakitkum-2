print("Weekly Exercise 3")

lama_kerja = 10 #10 tahun lama kerja
jam = 8 # 8 jam kerja perhari
gaji = 30000 #gaji perjam
bA1= 31 #jumlah hari jika berangkat satu bulan full dalam bulan Agustus
bA2=28 # jumlah hari jika tidak berangkat 3 hari dalam bulan Agustus
a =  5 # karyawan yang berkerja selama 5 tahun
b = 10 # karyawan yang berkerja selama 10 tahun
t=(10/100) # tunjangan sebesar 10%
l=(5*10000)

#Soal no 1
if bA1<bA2:
    print(f"1. Jumlah gaji Dwi selama sebulan",(gaji*jam*bA1))
elif bA2<bA1:
    print(f"1. Jumlah gaji Dwi selama sebulan",(gaji*jam*bA2))

#Soal no 2
if a>b:
    print(f"2. Tunjangan Dwi adalah =",(gaji*jam*bA2)*t)
elif a<b:
    print(f"2. Tunjangan Dwi adalah =",(gaji*jam*bA2)*t)

#soal no 3
    print(f"3. Gaji Dwi Bulan Agustus + Lembur =",(gaji*jam*bA2)+l)

