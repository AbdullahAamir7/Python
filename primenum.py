num=int(input("Enter the number: "))
if num < 1:
    for i in range(2,int(num**0.5)+1):
        
        if(num % i==0):
            print("Its not a Prime Number.")
    else:
     print(num," is a Prime number.")
else:
    print(num,"is not a prime number")            