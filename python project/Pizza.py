import datetime#date time libary for furthure use
now= datetime.datetime.now()
dmt= str(now)

print("-"*75)
print("\t\t Welcom to Pizza Hut")
print("-"*75)
name= input("Enter your Name:")
print("Enter your selection")
print("1) Small")
print("2) Medium")
print("3) Large")
sel= int(input("Please Enter yur selection:"))
tast= int(input("Veg(1)/Non-veg(2)?:"))

if sel == 1 :
    pizza= str("Small")
    cost= 150
elif sel == 2:
    pizza= str("Medium")
    cost=210
elif sel == 3 :
    pizza= str("Large")
    cost=290

if sel == 1 & tast == 2 :
    cost= 180
if sel == 2 & tast == 2 :
    cost= 250
if sel == 3 & tast == 2:
    cost= 340

if tast == 1 :
    typ= str("Veg")
else :
    typ = str("Non-Veg")

tax= cost + (cost*10/100)

print("-"*75)
print("\t\t\t Pizza Hut")
print("-"*75)
print(dmt)
print()
print("Costumour name:",name)
print("Selection:",pizza)
print("type:",typ)
print("Cost:",cost)
print("Tax = 10%")
print("total Amount=",tax)
print()
print("-"*75)



    


