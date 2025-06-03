#soal no 1
banyak_siswa = int(input("masukan banyak nya siswa: "))

print(f"banyak nya siswanya {banyak_siswa}")

list_nilai_siswa = []
for a in range(banyak_siswa):

    nilai_siswa = int(input("masukan nilai siswa: "))
    list_nilai_siswa.append(nilai_siswa)
    
    
rata_rata = sum(list_nilai_siswa) // banyak_siswa    
print(f"rata rata nya adalah {rata_rata:.2f}")
    
#soal no 2
in_suhu = input("masukan nilai suhu celcius: ")
celcius = int(in_suhu)

fahrenheit = (celcius * 9/5) + 32
kelvin = celcius + 273.15

print(f"nilai fahrenheit nya {fahrenheit:.2f}, nilai kelvin nya {kelvin:.2f}")