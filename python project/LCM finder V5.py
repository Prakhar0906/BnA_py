import numpy

def LCM(nums):
    print(nums)
    primes= (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97)
    factors= []
    i, div_val=0, 0 #begin from start 
    while nums[:] != []:
        print("number is",nums[i])
        print("Divisior is ",primes[div_val])

        if nums[i] in primes == True and nums[i] not in factors == True:  #speed boost to remove any present primes
            factors.append(nums[i])
            nums.remove(nums[i])
            i,div_val=0, 0 #reset 
            continue
        
        if nums[i] % primes[div_val] == 0: #if the prime is a factor of current number
            factors.append(primes[div_val]) #factor found 
            temp= map(lambda x=nums[i], y= primes[div_val] : int(x / y) if x % y == 0 else x , nums) #divide all
            g= list(temp)
            print(g)
            nums[0:]= g.copy() #convert to list, have new list 
            print(nums)
            i, div_val=0, 0 #reset the first number and the prime value              
        else:
            if i < (len(nums) - 1): # if we have not bin through all the nums
                i+=1
            else:
                div_val+=1 #try next prime 
                i=0
            
        for m in nums:
            if m == 1: #speed boost to remove ones 
                nums.remove(m)
                i=0
        

    return numpy.prod(factors) 
                                  

print(LCM([2, 3, 7]))

