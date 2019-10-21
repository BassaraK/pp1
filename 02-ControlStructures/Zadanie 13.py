x = int(input("Podaj liczbę x: "))
y = int(input("Podaj liczbę y: "))

if x>0 and y>0:
    print("Punkt leży w I ćwiartce")
elif x<0 and y>0:
    print("Punkt leży w II ćwiartce")
elif x<0 and y<0:
    print("Punkt leży w III ćwiartce")
elif x>0 and y<0:
    print("Punkt leży w IV ćwiartce")
elif x==0 and y!=0:
    print("Punkt leży na osi X")
elif x!=0 and y==0:
    print("Punkt leży na osi Y")
elif x==0 and y==0:
    print("Punkt leży w miejscu 0,0")