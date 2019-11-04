import random
tab = []
suma=0
def rzucKostka():
    for i in range(3):
        tab.append(random.randint(1,6))
    return tab
rzucKostka()
print("Wyrzucone oczka: ",tab)
for i in range(len(tab)):
    suma+=tab[i]
print("Suma oczek: ",suma)
