i=1
with open('C:/Users/Kacper Bassara/Desktop/pp1/03-FileHandling/NoEducation.txt','r') as file:
    for line in file:
        print(i,line, end='')
        i+=1