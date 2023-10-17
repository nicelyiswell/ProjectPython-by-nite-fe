kilograms = float(input())
centimeters = float(input())

meters = centimeters / 100
bmi = kilograms / meters**2
bmi = round(bmi, 2)


print(bmi)
if bmi < 18.5:
    print("Below normal weight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Class I Obesity")
elif bmi < 40:
    print("Class II Obesity")
else:
    print("Class III Obesity")