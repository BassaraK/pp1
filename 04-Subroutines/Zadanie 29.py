import statistics
tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]

def mediana(tab):
    tab.sort()
    if len(tab)%2!=0:
        marker=int((len(tab)/2)-0.5)
        print("Mediana = ",tab[marker])
    elif len(tab)%2==0:
        marker1 = int(len(tab)/2-1)
        marker2 = int(len(tab)/2)
        wynik = (tab[marker1]+tab[marker2])/2
        print("Mediana = ",wynik)
        
def dominanta(tab):
    print("Dominanta = ",statistics.mode(tab))



mediana(tab)
dominanta(tab)
