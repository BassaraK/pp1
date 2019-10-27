x = str(input("Wpisz dowolny ciąg znaków: "))
i = len(x)-1
wynik = [""]*len(x)
j=0

while i>=0:
    wynik[j]=x[i]
    j+=1
    i-=1
    
print(wynik)