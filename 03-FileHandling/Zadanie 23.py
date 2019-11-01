import re

with open('C:/Users/Kacper Bassara/Desktop/pp1/03-FileHandling/land.txt','r') as file:
    string=file.read()
digits = re.findall("\d",string)
suma = 0
for i in range(len(digits)):
    suma+=int(digits[i])
    
print(suma)