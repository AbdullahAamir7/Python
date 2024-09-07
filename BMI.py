weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in cm: "))

BMI= weight / (height / 100)**2

print("Your BMI is : ",BMI)

if BMI<=29:
    print("Your are Healthy")
elif BMI<=24:
    print("you are underweight") 

elif BMI<=19:
    print("you are weak") 

else:
    print("you are very weak") 

