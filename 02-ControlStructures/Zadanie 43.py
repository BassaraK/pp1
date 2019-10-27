a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

if a<c and a>b:
    print(b,a,c)
    
elif a>c and a<b:
    print(c,a,b)
    
elif b>c and b<a:
    print(c,b,a)
    
elif b>a and b<c:
    print(a,b,c)
    
elif c>a and c<b:
    print(a,c,b)
    
elif c>b and c<a:
    print(b,c,a)