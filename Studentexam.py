name=str(input("Enter Your name: "))
marks=int(input("Enter your percentage of matric: "))
attendence=float(input("Enter percentage of Attendence: "))
print("Your name is : ",name)
print("Your marks are : ",marks)
print("Your attendence is : ",attendence)
if (marks > 60):
    print("Marks is upto 60%")
    if (attendence > 75):
        print("Your attendence is upto 75%")
        print("\b Congratulation You are elligible for exams ")
    else:
     print("You are not elligible")
else:
    print("You are not Elligible")