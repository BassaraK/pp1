tab = []
n=1
while n>0:
    n = int(input("Podaj liczbe(0 kończy wczytywanie): "))
    tab.append(n)

tab.remove(0) 

def repetition(tab):
    for i in range(len(tab)):
        marker=0
        for j in range(len(tab)):
            if tab[i]==tab[j]:
                marker+1
        if marker>1:
            n=tab[i]
            tab.remove(n)
    print(tab)

repetition(tab)
