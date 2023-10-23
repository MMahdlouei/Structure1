import constans as c
from helper import *

#Triggering the entire project
#Do this by python run.py

def run():
    prime = calculate_primes(start = c.START, finish = c.FINISH)
    print(prime)
 

if __name__ == '__main__':
    run()