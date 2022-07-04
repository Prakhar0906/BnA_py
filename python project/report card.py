import datetime
now=datetime.datetime.now()
dmt= str(now)

name= input("Enter the Name of student:")
surname= input("Enter the sirname:")
clas= input("Enter the class:")
div= input("Enter the division:")
mob= int(input("Enter the mobile Number:"))
lan= int(input("Enter the Landline Number"))

print("-"*75)
print("")
print("\t\t\t Report Card")
print("")
print("Date:",dmt)
print("")
print("-"*75)
print("")
print("Name \t\t :",name,"\t\t Sirname \t :",surname)
print("")
print("Class \t\t :", clas, "\t\t\t Section \t :",div)
print("")
print("Telephone no.\t :", mob,"\t\t MB.No: \t :",lan)
print("")
print("-"*75)


