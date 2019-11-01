tab = []
suma = 0
with open('C:/Users/Kacper Bassara/Desktop/pp1/03-FileHandling/numbersinrows.txt','r') as file:
    for line in file:
        x = line.split(",")
        for i in range(len(x)):
            tab.append(x[i])
            suma+=int(x[i])
print(len(tab),suma)