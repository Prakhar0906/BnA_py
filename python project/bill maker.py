import datetime#date time libary for furthure use
now= datetime.datetime.now()
dmt= str(now)
#Obtaining the raw values
name= str(input("Enter customer's Name:"))
sp= float(input("Enter Net Amout:"))
#calculating the values
if sp <= 20000:
    discount= 10
if sp >= 25000:
    discount= 17.5

dis= sp*discount/100
preamount= sp-dis
staxpre= float(input("Enter the Sails tax"))
stax= preamount*staxpre/100
amount= preamount+stax
#Interface
print("-"*70)
print("\t\t\t Advance Store")
print(dmt)
print("-"*70)
print("Name:",name)
print("Bill Value=",sp)
print("Discount at",sp,"is",discount,"%")
print("Discount amount= Rs",dis)
print("Amount after discount=",preamount)
print("Sails tax=",staxpre,"%")
print("Sails tax in Rs=", stax)
print("")
print("-"*70)
print("\t\t\t\t Total amount=",amount)
print("-"*70)
