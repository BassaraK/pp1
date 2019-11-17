n = int(input("Podaj liczbe n: "))
x = int(input("Podaj początek zakresu: "))
y = int(input("Podaj koniec zakresu: "))

def sprawdzanie(n,x,y):
    if n>x and n<y:
        print("Liczba mieści sie w zakresie")
    else:
        print("Liczba nie mieści się w zakresie")

sprawdzanie(n,x,y)