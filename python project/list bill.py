name= str(input("Enter  the name:"))
lis= [input("Enter Item names:")]
cos= [input("Enter the cost:")]
sp= int(input("Enter the Sp"))

if sp <= 20000 :
    dis=10
if sp >=25000 :
    dis= 17.5

discount= sp*dis/100
preamount= sp- discount
staxr=float(input("Enter the Sails tax"))
stax= preamount*staxr/100
namount= preamount+stax

print("-"*70)
print()
print("-"*70)
print(lis/n)
