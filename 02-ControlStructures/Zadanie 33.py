liczba = str(input("Podaj liczbę: "))
tabela = ["zero","jeden","dwa","trzy","cztery","pięć","sześć","siedem","osiem","dziewięć"]
wynik = [""]*len(liczba)
for i in range(len(liczba)):
    bufor = int(liczba[i])
    wynik[i]=tabela[bufor]
print(wynik)