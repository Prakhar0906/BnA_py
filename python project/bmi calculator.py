import datetime#date time libary for furthure use
now= datetime.datetime.now()
dmt= str(now)

print("-"*75)
print("\t\t\t Know your Nutritional Status ")
print("-"*75)

print("Please Fill your personal details")

name= input("Enter your name:")
gen= input("Enter your gender(male or female):")
weight= float(input("Enter your weight in Kgs:"))
age= int(input("Enter your age:"))
height= float(input("Enter yor height in meters:"))

bmi= float(weight/(height*height)) #bmi calculator

if weight <= 18.5 : # weght status
    weightstat= "undreweight"
    
elif weight > 25 :
    weightstat= "overweight"

elif weight >= 30 :
    weightstat= "obsed"

else :
    weightstat= "normal"


print()# interfacing
print("-"*75)
print("\t\t\t Your Nutrition Report")
print("-"*75)
print()
print("Report as of",dmt)
print()
print("Name :\t",name)
print("Gende:\t",gen)
print("Age  :\t",age)
print("Weight=\t",weight)
print("Height=\t", height,"m")
print()
print("Your Body Mass Index=",bmi)
print("Your weight status:",weightstat)
print()
print()
print()
print("-"*75)









