while True:  
    choise= int(input("Enter the choise(1 for enter, 2 for send, 3 for exit):"))
    if choise == 1:
        bit=  input("Enter the bits:")
        bits= list(bit)
        print(bits)
    if choise == 2:
        for i in bits:
            print(i)
            
        

