wiek=int(input("Ile masz lat:"))
imie=str(input("Jak masz na imie:"))
#------------------SPRAWDZANIE WIEKU   \/
if wiek>10:
    print("Masz więcej niż 10 lat")
else:
    print("Masz mniej niz 10 lat")
if wiek>18:
    print("Jesteś pełnoletni")
else:
    print("Nie jesteś pełnoletni")
#------------------PĘTLE Z IMIENIEM    \/
print("---------------------")
for x in range(5):
    print(imie)
print("---------------------")
i = 0
while i < 5:
    print(imie)
    i+=1