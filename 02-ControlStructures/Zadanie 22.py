suma=0
ilosc=0
tab = [15,8,31,47,2,19]

for i in range(len(tab)):
    if tab[i]%2!=0:
        suma+=tab[i]
        ilosc+=1
    
print("Średnia arytmetyczna liczb nieparzystych wynosi",suma/ilosc)