pesel=str(input("Podaj numer pesel: "))
plec=int(pesel[9])
wiek=int(pesel[0:1])
if plec%2==0:
    print("Kobieta")
else:
    print("Mężczyzna")
if wiek<19:
    print(wiek)