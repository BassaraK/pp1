with open('C:/Users/Kacper Bassara/Desktop/pp1/03-FileHandling/students.txt','r') as file:
    for line in file:
        x = line.split(",")
        if x[2].isdigit() and int(x[2])<30:
            first = x[0]
            last = x[1]
            mail = x[4]
            print(first,last,mail)
        