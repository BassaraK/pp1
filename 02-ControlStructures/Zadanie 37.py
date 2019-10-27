a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

if a>b and a<c or a<b and a>c:
    print("Mediana wynosi: ",a)
    
elif b>a and b<c or b<a and b>c:
    print("Mediana wynosi: ",b)
    
elif c>a and c<b or c<a and c>b:
    print("Mediana wynosi: ",c)
