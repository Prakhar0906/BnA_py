from matplotlib import pyplot as plt

#aAssign y a equasion 
#give y a value
#solve for x 
#y= 'x^2-3x-4'
#equation= [char for char in y]
#print(equation)

px=[]
py=[]

for x in range(-2,6):
    y= (x*x)-(3*x)-4
    print(f"If x is {x} than y is {y}")
    px.append(x)
    py.append(y)


print(px)
print(py)
plt.xlim((-9,9))
plt.ylim((-9,9))
plt.plot([-8,8],[0,0], linewidth=2, color= 'red')
                 #x, #y
plt.plot([0,0],[-8,8], linewidth=2, color='red')
plt.plot(px,py, label='path')
plt.show()
    
    
