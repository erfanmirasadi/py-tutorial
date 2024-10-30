print("part1 :")

is_not_zero = True
counter  =  0
index = 0

while is_not_zero :
    user_number = int(input("enter a number to sum : "))
    
    if user_number == 0:
        is_not_zero = False
        print (f"avarage number is : {counter / index} ")
        
        break
    index += 1
    counter += user_number
    
        

        
        
        

        
            




    