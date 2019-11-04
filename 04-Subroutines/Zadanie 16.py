tab = []

def czytajLiczbe():
    suma=0
    for i in range(2):
        tab.append(int(input("Podaj liczbe: ")))
    for x in range(len(tab)):
        suma+=tab[x]
    print(suma)
czytajLiczbe()

