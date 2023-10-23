import constans as c
#Funcitons that are going to help calculate prime numbers
def is_prime(num):
    if num > 1:
        for n in range(2, num):
            if num % n != 0:
                #Keep on checking 
                continue
            else:
                return False
        return True

def calculate_primes(start, finish):
    primes = []
    for n in range(start, finish):
        if is_prime(n) and n not in c.SKIP_RANGE:
            primes.append(n)
    return primes
