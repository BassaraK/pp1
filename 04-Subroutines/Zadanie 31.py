tab = [2, 5, 4, 1, 8, 7, 4, 0, 9]

def reverse(tab):
    tab2=[]
    i=len(tab)-1
    j=0
    while i>=0:
        tab2.append(tab[i])
        j+=1
        i-=1
    print("",tab,"\n",tab2)

reverse(tab)


