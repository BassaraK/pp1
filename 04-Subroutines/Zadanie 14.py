x = 23
y = [15,38,7,23,14]
marker=0
def f(x,y):
    print("Liczba: ",x)
    print("Tablica: ",y)
    marker=0
    for i in range(len(y)):
        if x==y[i]:
            marker+=1
    if marker>0:
        print("Rezultat: Podana liczba występuje w tablicy")
    else:
        print("Rezultat: Podana liczba nie występuje w tablicy")
f(x,y)

