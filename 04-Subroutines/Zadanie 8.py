tab = [4,3,7,1,3]

def funkcja(tab):
    suma=0
    print(tab)
    for i in range(len(tab)):
        suma+=int(tab[i])
    print(suma)


funkcja(tab)