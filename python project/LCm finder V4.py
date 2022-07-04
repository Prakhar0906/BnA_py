
def LCM(nums):
    print(nums)
    primes= (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97)
    factors= []
    div_val= 0
    temp= []
    times= len(nums)
    #print(f"the length of list is {times}")
    i=0
    till=[]
    till.extend([1 for i in range(len(nums))])
    while nums[:] != till: #do this for the number of elements in        
        print("i is",i)
        print("number is",nums[i])
        print(f"prime is {primes[div_val]}")
        if (nums[i] % primes[div_val] == 0):   
            factors.append( primes[div_val] )                                          
            print(f"The {primes[div_val]} has been appended")
            for x in nums:
                if x % primes[div_val] == 0:
                    val= int(x/primes[div_val])                     
                    temp.append(val)
                else:
                    temp.append(x)
            print(temp)
            nums.clear()
            nums[0:]= temp.copy()
            temp.clear()
            i=0
            div_val=0
            rep=0
        else:
            print("not divisible")
            if i < (times-1):
                i+=1
            else:
                div_val+=1
                i=0
        for m in nums:
            if m == 1:
                nums.remove(m)
                print(f"{m} has been removed")
                print(nums)
                i=0
        till.clear()
        till.extend([1 for l in range(len(nums))])
        times= len(nums)

    
    return factors

print(LCM([32,124,728]))
