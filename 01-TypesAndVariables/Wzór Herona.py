import math
a = int(input("Podaj bok a trójkąta: "))
b = int(input("Podaj bok b trójkąta: "))
c = int(input("Podaj bok c trójkąta: "))
p = 0.5*(a+b+c) #połowa obwodu trójkąta
pole = p*math.sqrt((p-a)*(p-b)*(p-c))

print("Pole trójkąta wynosi:",pole)