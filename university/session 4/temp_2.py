print("part 3 :")

def collatz(n):
    max_number = n
    #print(f"Please enter a number: {n}")
    
    while n != 1:
        print(n, end= " ")
       
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
            
        max_number = max(max_number, n)
        
       
    
    return max_number




user_number = int(input("plaese Enter a number: \n"))


finall_number = collatz(user_number)

print(f"\nThe maximum number you get is: {finall_number}")