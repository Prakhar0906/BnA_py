print("Number adder")
pre_val= 0
num1= int(input("Enter num 1"))
num2= int(input("Enter num 2"))
isum= num1+num2
print(num1,"+",num2,"=")
print(isum)
pre_val= isum
print(pre_val)


while True :
    addmore = int(input("Add another number?(press 1 for yes)"))
    if addmore == 1:
     amn= int(input("Enter the number to be added"))
     ssum= isum+amn
     print(isum,"+",amn,"=")
     print(ssum)
     pre_val= ssum
     print(pre_val)
    else :
        break 

    
                    
