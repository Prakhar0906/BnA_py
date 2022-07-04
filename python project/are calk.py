print("Welcom To The Are calculator")
print("You have the following choises:-")
print("1)Square")
print("2)Rectangle")
print("3)Circle")
print("4)Triangle")

chois= int(input("Enter your selection in number"))

if chois == 1 :
    print("You chose Square")
    side= int(input("Enter side:"))
    per= side*4
    are= side*side
    print("Perimiter=",per)
    print("Area=",are)
elif chois == 2 :
    print("So you chose Rectangl")
    l= int(input("Enter length"))
    b= int(input("Enter breadth"))
    per= l+b*2
    are= l*b
    print("Perimiter=",per)
    print("Aera=",are)
elif chois == 3 :
    print("So you Chose Circle")
    r= int(input("Enter Radius"))
    per= 2*22*r/7
    are= r*r*22/7
    print("Preimiter=",per)
    print("Area=",are)
elif chois == 4 :
    print("So you chose triangle")
    base= int(input("Enter Base"))
    height= int(input("Enter Height"))
    are= base*height/2
    print("Area=",are)
else :
    print("invalid input")
           
    
