
def LCM(nums):
    print(nums)
    primes= (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97)
    factors= []
    div_val=0
    temp= []
    times= range(len(nums))
    for i in times :#if any number is divisible by the currnt prime
        print(i)
        print(f"the picked number is {nums[i]}")
        picked_num= nums[i]
        if  picked_num % primes[div_val] == 0 :             
            factors.append(primes[div_val])       #append the prime in factors 
            print(f"it is divisible by {primes[div_val]}")
            for x in nums:                        #divide all other numbers by the prime
                if x % primes[div_val] == 0:      #if number is divisible divide
                    temp.append(int(x/primes[div_val]))#make a temperory list
                    print(f"{x} divided by {primes[div_val]}is {x/primes[div_val]}")
                    div_val=0                     #reset the prime
                    print(f"Now the div_val is{div_val}")
                else:                             #else 
                    temp.append(x)                #add the number itself to the temp list
                                       #incriment the prime to next

            nums.clear()
            nums[0:] = temp.copy()
            temp.clear()
            print(nums, temp) 
        else:
            div_val= div_val+1
            print(f"div_val is {div_val} so the number is{primes[div_val]}")
            times=0
            
    return factors

print(LCM([21,14,62]))
                       
