import math #library untuk operasi matematika

luas_lingkaran = lambda r: math.pi * r*r
#lambda : .....

luaslingkaran = lambda r: 3.14 * r ** 2

jari_jari = float(input("Masukkan jari-jari lingkaran: "))

print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luaslingkaran(jari_jari)}")