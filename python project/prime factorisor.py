import copy
primes= (2,3,5,7,11,13,17,19,23,29)
number= int(input("Enter the number:"))
factors= []
res=0

for j in range(len(primes)):
    i= primes[j]
    print(f"i= {i}")
    if number == 1:
        break
    else:
        if number % i == 0:
            questiont= int(number/i)
            #questiont= number
            print(f"{number} divided by {i} is {questiont}")
            factors.append(i)
            number= questiont
            print(number)
            continue
            
        
        
print(factors)
