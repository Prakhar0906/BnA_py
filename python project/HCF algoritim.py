#HCF Finding algorithim of two number using Euclid's division algorithim 
num1= int(input("Enter The First Number:"))
num2= int(input("Enter the second Number:"))

if num1>num2:
    a=num1
    b=num2
else:
    a=num2
    b=num1


q=int(a/b)
r= a-(b*q)
print("Divident(a)=",a)
print("Divisior=(b)",b)
print("Quetiont=(q)",q)
print("Remainder=(r)",r)

while (r != 0):
    a=b
    b=r
    q= int(a/b)
    r= a-(b*q)
    print()
    print("Divident(a)=",a)
    print("Divisior=(b)",b)
    print("Quetiont=(q)",q)
    print("Remainder=(r)",r)
    print()

print("HCF=",b)
    
    

