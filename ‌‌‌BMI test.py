weight = float(input("please enter weight(kg): "))
height = float(input("and height(m) for exampel-> 1.65:  "))

#BMI = weight / ((height/100) ** 2) --> for height(cm)

BMI = (weight / (height * height))
if BMI < 18.5:
    result = "Underweight!"
elif BMI >= 18.5 and BMI < 25:
    result = "Normal!"
elif BMI >= 25 and BMI < 30:
    result = "Overweight!"
elif BMI >= 30 and BMI < 35:
    result = "Obese!"
elif 35 < BMI:
    result = "Extremely Obese!"

print("BMI=", BMI)
print("result=", result)
