def prime(n):
    if  n < 0:
        return "There is no prime for negative"
    elif n == 0 or n == 1:
        return "No prime"
    else:
        isprime = True
        for i in range(2, n):
            if n % i == 0:
                isprime = False
                break
        
        
        if isprime:
            print(f"The num {n} is Prime Number")
        else:
            print(f"The num {n} is not a prime nunber")
            
prime(9)
                