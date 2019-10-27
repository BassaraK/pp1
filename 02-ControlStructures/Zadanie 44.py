maks = int(input("Podaj limit prędkości (km/h): "))
speed = int(input("Podaj prędkość pojazdu (km/h): "))
if speed<maks:
    print("Nie przekroczono prędkości")
elif (speed-maks)<10:
    print("Mandat (zł): ",(speed-maks)*5)
else:
    print("Mandat (zł): ",((speed-maks-10)*15)+50)