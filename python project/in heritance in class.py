
class Pet:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def show(self):
        print(f"I am {self.name} I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super()
        self.color= color
    
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p= Pet("Tim", 19)
p.show()

c= Pet("Bill", 35)
c.show()

d= Dog("Jill", 25)
d.show()


m= Cat("Maui", 13)
m.show()
m.speak()
d.speak()

f= Fish("Bubbles", 100)
f.speak()
