import re

komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
suma=0

for i in range(len(cyfry)):
    suma+=int(cyfry[i])
    
print("Średnia temperatura w następnych ",len(cyfry)," wynosi: ",suma/len(cyfry))