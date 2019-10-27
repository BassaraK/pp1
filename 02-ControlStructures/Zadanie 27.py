marker=0
i=1
while i<10:
    if i==0:
        break
    print("*"*i)
    if i<5:
        if marker==1:
            i-=1
            continue
        else:
            i+=1
    elif i>=5:
        marker=1
        i-=1