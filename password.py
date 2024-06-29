import random

karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parolauzunluk = int(input("parola uzunlugu: "))

parolagirme = ""

for _ in range(parolauzunluk):
    parolagirme += random.choice(karakter)

print("parolagirme:", parolagirme)
