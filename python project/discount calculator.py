sp= float(input("Enter the Cost"))

if sp <= 20000:
    discount= 10
if sp >= 25000:
    discount= 17.5

dis= sp*discount/100
netpay= sp-dis
staxval= float(input("Enter the sails tax:"))
stax= netpay*staxval/100
pay= netpay+stax
print("Amount paied=",sp)
print("Discount at", sp,"is",discount,"%=",dis)
print("Cost after discount=", netpay)
print("Sails tax=",staxval,"% which equals to ",stax)
print("Total amount to be pied=",pay)

