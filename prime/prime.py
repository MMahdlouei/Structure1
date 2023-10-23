from prime.helper import *
import prime.constans as c

class Prime:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def calculate_primes(self):
        primes = []
        for n in range(self.start, self.finish):
            if is_prime(n) and n not in c.SKIP_RANGE:
                primes.append(n)
        return primes

    def Prettify(self):
        body = ''
        for results in self.calculate_primes():
            body += f"This is a prime number: {results} \n"
        return body
