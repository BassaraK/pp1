month = ["Nie ma miesiąca 0","Styczeń","Luty","Marzec","Kwiecień","Maj","Czerwiec","Lipiec","Sierpień","Wrzesień","Październik","Listopad","Grudzień"]
numbers = []
result = []
n=1


while n>0:
    n = int(input("Podaj numery miesięcy(0 kończy wczytywanie): "))
    numbers.append(n)
numbers.remove(0)

def miesiąc(numbers):
    for i in range(len(numbers)):
        result.append(month[numbers[i]])
    for i in range(len(result)):
        print(numbers[i],"=",result[i],end="  |  ")
miesiąc(numbers)