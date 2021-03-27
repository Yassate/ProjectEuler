import math

def is_prime(number):
    if number%2 == 0 or number%3 == 0:
        return False
    divisors_range = range(5, int(math.sqrt(number))+1, 6)
    for div in divisors_range:
        if (number%div == 0) or (number%(div+2) == 0):
            return False
    return True

in_number = 600851475143
divisors_range = reversed(range(2, int(math.sqrt(in_number))+2))
div = int(math.sqrt(in_number))+1
factors = list()

while div > 2:
    if(in_number%div) == 0:
        factors.append(div)
        factors.append(in_number%div)          
    div = div-1

for i, factor in enumerate(factors):
    if not is_prime(factor):
        factors.pop(i)
        
print(f"Highest prime factor: {max(factors)}")

