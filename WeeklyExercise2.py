print("Weekly Exercise 2")
a1=85
b1 = 80
c1= 75
d1= 95
e1 = 85
f1 = 75
g1 = 70
h1= 85
i1 = 80

a2= 75
b2= 90
c2= 80
d2= 80
e2= 85
f2= 90
g2= 75
h2= 85
i2= 75

# import module
from tabulate import tabulate

# assign data
mydata = [
["Shafira",a1,a2],
["Amanda",b1,b2],
["Aditya",c1,c2],
["Nedia",d1,d2],
["Widya",e1,e2],
["Hanif",f1,f2],
["Andi",g1,g2],
["Dhanar",h1,h2],
["Hikma",i1,i2],
]

# create header
head = ["Name", "Kalkulus1","M.Statistika",]

# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))


rata=(a1+a2)//2
print("1.Rata-rata nilai Safira =",rata)
jumlah = (f1+f2+g1+g2)
print("2.Jumlah nilai Hanif dan Andi =",jumlah)
rata_nilai_kalkulus =(e1+h1+i1+d1)//4
print("3.Rata-rata nilai Kalkulus 1 Wdiya,Dhanar,Hikma,Nedia =",rata_nilai_kalkulus)
rata_nilai_mStatistika =(e2+h2+i2+d2)//4
print("  Rata-rata nilai Metode Statistika Wdiya,Dhanar,Hikma,Nedia =",rata_nilai_mStatistika)
rata_kalkulus = (a1+b1+c1+d1+e1+f1+g1+h1+i1)//9
print("4.Rata nilai Kalkulus 1 =",rata_kalkulus)
rata_mStatistika = (a2+b2+c2+d2+e2+f2+g2+h2+i2)//9
print("5.Rata nilai Metode Statistika =",rata_mStatistika)