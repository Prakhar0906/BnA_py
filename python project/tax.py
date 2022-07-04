salary= float(input("Enter your salarey"))

if salary <= 50000:
    tax= 5/100*salary
    print("Tax=",tax)
elif salary <=  60000 :
    tax= 7/100*salary
    print("Tax=",tax)
elif salary <= 70000 :
    tax= 8/100*salary
    print("tax=",tax)
elif salary <= 8000 :
    tax= 9/100*salary
    print("tax=",tax)
else :
    print("invali input")
 
