i=1
while i<31:
    if i%3==0 and i%5==0:
        print("BINGO")
    elif i%3==0:
        print("THREE")
    elif i%5==0:
        print("FIVE")
    else:
        print(i)
    i+=1