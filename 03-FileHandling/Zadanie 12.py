produkt = str(input("Podaj produkt do dodania: "))
file = open("C:/Users/Kacper Bassara/Desktop/pp1/03-FileHandling/shoppinglist.txt","a")
file.write(produkt)
file.write("\n")
file.close()
