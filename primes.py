"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def isPrime(n):
    if n == 2 or n == 3 :
        return True
    elif n % 2 == 0 or n % 3 == 0 :
        return False 
    i = 5
    while i * i <= n :
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i+=6
    return True

def primes(number_of_primes):
    if (number_of_primes < 1):
        raise ValueError("Enter a valid number please")
    list = []
    #all prime numbers are greater than one
    current_number = 2
    while len(list) < number_of_primes:
        if isPrime(current_number):
            list.append(current_number)
        current_number+=1
        
    return list
