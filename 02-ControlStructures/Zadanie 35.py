import math
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

delta = b**2-(4*(a*c))

if delta>0:
    x1=(-b-math.sqrt(delta))/(2*a)
    x2=(-b+math.sqrt(delta))/(2*a)
    print("x1 = ",x1," x2 = ",x2)
    
elif delta==0:
    x1=(-b)/(2*a)
    print("x1 = ",x1)
    
else:
    print("Nie ma pierwiastków")