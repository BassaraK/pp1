def suma(n):
    razem=0
    for i in range(1,n+1):
        razem+=i
    print(razem)
n = int(input("Podaj zakres: "))
suma(n)