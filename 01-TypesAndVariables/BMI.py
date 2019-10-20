wzrost = 179
cal=0.393700787
print("Mam",wzrost,"cm wzrostu tj.",wzrost*cal/12,"stóp")

wzrostBMI = int(input("Podaj wzrost w cm:"))/100
wagaBMI = int(input("Podaj wagę w kg:"))
BMI = (wagaBMI/(wzrostBMI*wzrostBMI))
if BMI<18.5:
    print("Wskaźnik BMI:",BMI,"(niedowaga)")
elif BMI>25:
    print("Wskaźnik BMI:",BMI,"(nadwaga)")
else:
    print("Wskaźnik BMI:",BMI,"(waga prawidłowa)")
