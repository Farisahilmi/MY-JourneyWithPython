#operator aritmatika
a = 1 + 2 #tambah
b = 2 - 3 #kurang
c = 2 * 2 #kali
d = 12 / 3 #hasil bagi desimal
e = 12 // 3 #hasil bagi bulat
f = 11 % 3 #modulus
g = 2 ** 2 #pangkat

print(a) #3
print(b) #-1
print(c) #4
print(d) #4.0
print(e) #4
print(f) #2
print(g) #4


"""*Urutan operator aritmatika (dari yang pertama dieksekusi)*
1.tanda kurung / dalam kurung = ()
2.pangkat = **
3.perkalian, pembagian, pembagian bulat, dan modulo = *, /, //, %
4.penjumlahan dan pengurangan = +,-"""

#Operator Perbandingan (relasional)
#membandingkan dua nilai

a = 1 == 1 #sama dengan
b = 1 != 2 #tidak sama dengan
c = 1 > 2 #lebih besar
d = 1 < 2 #lebih kecil
e = 1 >= 2 #lebih besar atau sama dengan
f = 1 <= 2 #lebih kecil atau sama dengan

z = 1 <= 2 or (1>= 2)
print(z)

"""*Urutan operator perbandingan*
1.semua operator perbandingan memiliki prioritas yang sama
2.jika ada lebih dari satu operator perbandingan, mereka dievaluasi dari kiri ke kanan, tidak ada operator yang diprioritaskan lebih dulu 
3.namun, kita bisa menggunakan tandan kurung () untuk mengatur urutan eksekusi jika diperlukan"""

#operator penugasan (assignment)

a = 5 

a += 2 #7
a -= 2 #3
a *= 2 #10
a /= 2 #2.5
a //= 2 #2
a %= 2 #1
a **= 2

"""*Urutan operator penugasan*
1.operator penugasan itu sendiri tidak memiliki urutan prioritas yang lebih tinggi dalam kelompoknya
2.mereka hanya dieksekusi dalam urutan kiri ke kanan setelah operator lainnya"""

#operator logika
a = 2
b = 2

c = a and b #True
d = a or b #True
e = not a #False

print(c)
print(d)
print(e)

#operasi identitas
a = 1

b = 1 is a
c = 1 is not a

z = [1,2,4]

x = 5 is not z

print(x)

#operator keanggotaan
#memeriksa apakah nilai ada di dalam koleksi (list, string, dll)

a = [1,"sayur",3.2]

b = "sayur" not in a
print(b)

#operator bitwise
#bekerja pada level bit(biner)

#biner 1 & 0



a = 16
c = a >> 1


print(c)



# 128, 64, 32, 16, 8, 4, 2, 1



a = 5
b = 3

c = a >> b
print(c)









