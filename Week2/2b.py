weight_KG = float(input())
height_CM = float(input())

bmi = round(weight_KG/ ((height_CM/100)**2) ,2)


print(bmi)

if bmi < 18.5 :
    print("Below normal weight")
elif bmi < 25 :
    print("Normal weight")
elif bmi < 30 :
    print("Overwight")
elif bmi < 35 :
    print("Class I Obesity")
elif bmi < 40 :
    print("Class II Obesity")
else :
    print("Class III Obesity")  
    