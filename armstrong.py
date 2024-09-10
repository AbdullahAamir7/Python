number1=int(input("Enter 1st number: "))
number2=int(input("Enter 2nd number: "))
number3=int(input("Enter 3rd number: "))
ans=int(input("Enter number together"))
armstong1=number1**3
armstong2=number2**3
armstong3=number3**3
numans=armstong1+armstong2+armstong3
if (numans == ans):
    print(ans," is an Armstrong number.")
else:
    print(ans," is not an Armstrong Number.")    