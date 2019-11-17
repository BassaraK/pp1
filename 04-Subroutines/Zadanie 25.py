tab = ["Janek","Ania","Wojtek","Zosia"]
n = str(input("Podaj szukane imie: "))
print("Imiona: ",end="")
for i in range(len(tab)):
    print(tab[i], end=" ")
print('\n'+"Imie: "+n)

def funkcja(n):
    check=0
    for i in range(len(tab)):
        if tab[i]==n:
            check+=1
    if check>0:
        print("Rezultat: imie zawarte jest w wykazie imion")
    else:
        print("Rezultat: imie nie jest zawarte w wykazie imion")
funkcja(n)
