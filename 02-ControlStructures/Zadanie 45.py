n = int(input("Podaj ilość liczb pierwszych: "))
tab = [""]*n
for i in range(n):
    x=2
    while x<(i/2):
        if i%2==0:
            break
        else:
            tab[i]=i
            