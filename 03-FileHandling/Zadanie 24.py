tab = [['Imie','Nazwisko','E-mail'],['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'
],['Piotr','Wyga','wygap@gop.pl']]

with open('zadanie_24.csv','w') as file:
    for n in tab:
        for i in n:
            if i!=n[-1]:
                file.write(f'{i},')
            else:
                file.write(f'{i}\n')