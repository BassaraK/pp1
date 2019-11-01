tab = []
with open('C:/Users/Kacper Bassara/Desktop/pp1/03-FileHandling/numbers.txt','r') as file:
    for line in file:
        tab.append(int(line))
tab.sort()
print(tab)