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
