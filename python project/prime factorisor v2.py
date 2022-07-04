prim= (2,3,5,7,11,13,17,19,23,29)
num= int(input("Enter the number:"))
div_val=0
factors=[]
res=0
while res != 1:
    divident= prim[div_val]
    #print(divident, "", div_val)
    if num % divident == 0:
        res = num/divident
        print(f"{num} divided by{divident} is {res}")
        num = res
        print(res)
        div_val = 0
        factors.append(divident)
    else:
        div_val+=1
        
print(factors)
