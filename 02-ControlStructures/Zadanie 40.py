import random
a=0
b=0
c=0
d=0
e=0
f=0
for i in range(100):
    x=random.randint(1,6)
    if x==1:
        a+=1
    elif x==2:
        b+=1
    elif x==3:
        c+=1
    elif x==4:
        d+=1
    elif x==5:
        e+=1
    elif x==6:
        f+=1

print("Szóstka: ",f)
print("Piątka: ",e)
print("Czwórka: ",d)
print("Trójka: ",c)
print("Dwójka: ",b)
print("Jedynka: ",a)