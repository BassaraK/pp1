tab = ["Genowefa","Onufry","Celestyna","Alojzy","Pankracy","Teofil"]
i=0
dlugosc=0
marker=0
while i<len(tab):
    if len(tab[i])>dlugosc:
        marker=i
        dlugosc=len(tab[i])
    i+=1
print("Najdłuższe imię to: ",tab[marker])
    