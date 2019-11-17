dochod = int(input("Podaj dochód: "))
result=0
def podatek(dochod):
    if dochod<=5000:
        result=(dochod*0.17)
    elif dochod>5000:
        nadwyzka=dochod-5000
        result=(5000*0.17)+(nadwyzka*0.32)
    print("Podatek należny: ",result)
podatek(dochod)