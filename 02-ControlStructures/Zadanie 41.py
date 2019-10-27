count=-1
i=1
tab=[0]
suma=0
x=0
while i!=0:
    i=int(input("Podaj liczbę: "))
    tab.append(i)
    count+=1
    
for x in range(len(tab)):
    suma+=tab[x]
    
    
print("REZULTAT: Liczb=",count," Suma:",suma," Średnia:",suma/count)