tab = []
with open('C:/Users/Kacper Bassara/Desktop/pp1/03-FileHandling/universities.txt','r') as file:
    for line in file:
        tab.append(line)
tab.sort()

with open('C:/Users/Kacper Bassara/Desktop/pp1/03-FileHandling/universities.txt','w') as file:
    for i in range(len(tab)):
        file.write(str(tab[i]))
        file.write("\n")

