correct = "0805"
i=0
while i<3:
    pin=input("Podaj kod PIN: ")
    if pin==correct:
        print("Kod poprawny")
        break
    else:
        print("Kod PIN nie poprawny")
    i+=1
    if i==3:
        print("Karta płatnicza zostaje zablokowana")
        break
    