from collections import Counter

def LCM(numbers):
    for i in numbers:
        #print(factorise(i))
        lis= factorise(i)
        #print(lis)
        keys= Counter(lis).keys()
        Occur= Counter(lis).values()
        #print(list(keys))
        #print(Occur)
        print(dict(zip(keys, Occur)))
    pre_result= prod(lis)
    

def factorise(num):
    factors= []
    primes= (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97)
    div_val=0
    rem=0
    
    while rem != 1:
        divident= primes[div_val]
        if (num % divident == 0):
            rem = num/divident
            num = rem
            div_val=0
            factors.append(divident)
            
        else:
            div_val+=1
            
    return factors

#print(factorise(int(input("Enter the number:"))))
nums= input("Enter the numbers:")
res = [int(i) for i in nums.split() if i.isdigit()]
LCM(res)
