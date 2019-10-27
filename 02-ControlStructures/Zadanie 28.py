x = int(input("Podaj szerokość prostokąta: "))
y = int(input("Podaj wysokość prostokąta: "))

print("*"*x)
for i in range(y-2):
    print("*"," "*(x-4),"*")
print("*"*x)