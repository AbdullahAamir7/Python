def pictorialfunc(num):
    if num == 1:
        return inputnum
        
    else:
        return num * pictorialfunc(num-1)
    
inputnum=int(input("Enter the number: "))

if inputnum < 1:
    print ("The pictorial of 1 is 1")
elif inputnum == 0:
    print("There is no pictorial of 0. ")
else:
    print("The Pictorial of ",inputnum,"is: ",pictorialfunc(inputnum))        