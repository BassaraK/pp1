import random

throw=random.randint(1,6)
guess=int(input("Zgadnij wyrzuconą liczbę oczek:"))
if guess==throw:
    print("Zgadłeś!")
else:
    print("Komputer wyrzucił",throw,"Spróbuj jeszcze raz!")