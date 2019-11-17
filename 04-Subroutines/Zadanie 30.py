import random

print("Dla 1000 liczb losowych z przedziału <1,50>:")
tab = []

def losowanie(tab):
    parzyste=0
    nieparzyste=0
    for i in range(1000):
        tab.append(random.randint(1,50))
    for i in range(1000):
        if tab [i]%2==0:
            parzyste+=1
        else:
            nieparzyste+=1
    print("Parzyste: ",parzyste/10,"%","\nNieparzyste: ",nieparzyste/10,"%")


losowanie(tab)
