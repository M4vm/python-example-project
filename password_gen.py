import random

simboli = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$-_"

print(".")

while 1:
    duzina = int(input("Duzina: "))
    sifra  = ""
    for x in range(0,duzina):
        sranje = random.choice(simboli)
        sifra = sifra + sranje
    print(sifra)
    print(".")