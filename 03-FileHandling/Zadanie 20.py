tab = []
with open('C:/Users/Kacper Bassara/Desktop/pp1/03-FileHandling/numbers.txt','r') as file:
    for line in file:
        if int(line)%2==0:
            tab.append(int(line))
tab.sort()

with open('evennumbers.txt','w') as file:
    for i in range(len(tab)):
        file.write(str(tab[i]))
        file.write("\n")
