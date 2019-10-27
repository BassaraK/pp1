i=1
j=2
sp=0 #suma liczb parzystych
sn=0 #suma liczb nieparzystych
while i<51:
    sn+=i
    i+=2

while j<51:
    sp+=j
    j+=2
    
print("Suma liczb parzystych i nieparzystych wynosi odpowiednio:",sp,"i",sn)
