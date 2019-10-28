tab = [32,16,5,8,24,7]
with open('tablica.txt','w') as file:
    for i in range(len(tab)):
        file.write(str(tab[i]))
        file.write("\n")