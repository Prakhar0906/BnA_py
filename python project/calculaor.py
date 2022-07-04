print("Welcom to the calculator")
print("    by Prakhar")
pre_val= float(0) #previousely obtained value
while True :
    print("")
    print("(value 1 is for yes and all other are no)")
    print("Choose your opration")
    print("1)Addation")
    print("2)Subtraction")
    print("3)Multiplcation")
    print("4)Division")
    print("")
    print("Previousely obtained value=",pre_val)
    print("")


    selection= int(input("Enter your selection:")) #selection
    
    if selection == 1 :
        print("")
        print("So you chose to add")
        upv= int(input("use previous obtained value?:"))#use the prevousely obtained value?
        if upv == 1 : #yes/no?
            num1= pre_val #Number 1 is changed by previousely obtained value
            num2= float(input("Enter the number to be added:"))#number to be added to the value
            isum= pre_val+num2 #initial sum
            print(pre_val,"+",num2,"=")
            print(isum)
            pre_val= isum #replace the previousely obtained value by new value
        else :
            num1= float(input("Enter 1st number:"))
            num2= float(input("Enter 2nd number:"))
            isum= num1+num2
            print(num1,"+",num2,"=")
            print(isum)
            pre_val= isum
        while True: #This loop is fo repetative opration so user does not have to go through selection again
            addmore= float(input("add more?(press 1 for yes)")) #add more to the initial value 
            if addmore == 1 : #yes/no
                adm= float(input("Enter the number to be added:"))
                ssum= isum+adm
                print(isum,"+",adm,"=")
                print(ssum)
                pre_val= ssum
            else :
                break # break out of loop
            
    elif selection == 2 :
        print("")
        print("So you chose to subtract")
        upv= int(input("use previous obtained value?:"))
        if upv == 1 :
            num1= pre_val
            num2= float(input("Enter the number to be subtracted:"))
            isum= pre_val-num2
            print(pre_val,"-",num2,"=")
            print(isum)
            pre_val= isum
        else :
            num1= float(input("Enter 1st number:"))
            num2= float(input("Enter 2nd number:"))
            isum= num1-num2
            print(num1,"-",num1,"=")
            print(isum)
            pre_val= isum
        while True:
            submore= int(input("subtract more?(press 1 for yes)"))
            if submore == 1 :
                adm= float(input("Enter the number to be subtract:"))
                ssum= isum-adm
                print(isum,"-",adm,"=")
                print(ssum)
                pre_val= ssum
            else :
                break
    elif selection == 3 :
        print("")
        print("so you chose to multiply")
        upv= int(input("use previous obtained value?:"))
        if upv == 1 :
            num1= pre_val
            num2= float(input("Enter the number to be multiplied:"))
            isum= pre_val*num2
            print(pre_val,"*",num2,"=")
            print(isum)
            pre_val= isum
        else :
            num1= float(input("Entr 1st number:"))
            num2= float(input("Enter 2nd number:"))
            isum= num1*num2
            print(num1,"-",num1,"=")
            print(isum)
            pre_val= isum
        while True:
            mulmore= int(input("multiply more?(press 1 for yes)"))
            if mulmore == 1 :
                mulm= float(input("Enter the number to be multiplied:"))
                ssum= isum*mulm
                print(isum,"-",mulm,"=")
                print(ssum)
                pre_val= ssum
            else :
                break
    elif selection == 4 :
        print("")
        print("So you chose to divide")
        upv= int(input("use previous obtained value?:"))
        if upv == 1 :
            num1= pre_val
            num2= float(input("Enter the number to be divided by:"))
            isum= pre_val/num2
            print(pre_val,"/",num2,"=")
            print(isum)
            pre_val= isum
        else :
            num1= float(input("Enter divisor:"))
            num2= float(input("Enter divideant:"))
            isum= num1/num2
            print(num1,"/",num1,"=")
            print(isum)
            preval= isum
        while True:
            devmore= int(input("Divide more?(press 1 for yes)"))
            if devmore == 1 :
                devm= float(input("Enter the number to be divided by:"))
                ssum= isum/devm
                print(isum,"/",devm,"=")
                print(ssum)
                pre_val= ssum
            else :
                break
    else :
        break 
    
            
            
            
                  
                   
 
