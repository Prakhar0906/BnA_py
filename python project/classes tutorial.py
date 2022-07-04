#classes define object
#every thing is a object in python and methodes define what can be done on them
#for instance an int is a object and + defined it can be added with another int
#we can define our objects and by class method


class Dog:#something is in dog so following functions can be pufoemed on the thing
#self is to reference to whom, to diliver the value to correct caller 
    def __init__(self, name, age): #this method will run automatically whenever this object
        self.name= name       #is created and will immediately take in arguments  
        self.ages= age #self.ages is the main variable and age is the argument
    
    def add_one(self, x):
        return x+1
    
    def bark(self):
        print("bark")

    def get_age(self):
        return self.ages

    def get_name(self):
        return self.name
    def set_age(self, age):
        self.ages= age 

d= Dog("Rockey", 12)# this is a self made object and I can paform following methodes on it 
#print(d.add_one(5))#the . is for joining this is equilent to Dog(add_one(5))
print(type(d))
d2= Dog("Pug", 5)
print(d.get_name(), d.get_age())
print(d2.get_name(), d2.get_age())
d.set_age(4)
print(d.get_name(), d.get_age())
