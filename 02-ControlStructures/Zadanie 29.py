tab = [15,8,31,47,2,19]
print("tab: ",tab)
i=len(tab)-1
j=0
tab2=[0,0,0,0,0,0]
bufor=0
while i>=0:
    bufor=tab[i]
    tab2[j]=bufor
    i-=1
    j+=1
print("tab in reverse: ",tab2)