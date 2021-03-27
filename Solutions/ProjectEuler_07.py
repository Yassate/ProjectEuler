import math
import time

#by iteration (performance - 50 cycles in 157 sec)
def erastothenes(prime_range):
    main_array = [2] + list(range(3, prime_range, 2))
    i = 0

    while i < math.sqrt(prime_range):
        j = i + 1
        divisor = main_array[i]
        while j < len(main_array):
            element = main_array[j]
            if element%divisor == 0:
                main_array.pop(j)
            j = j + 1     
        i = i + 1
    return main_array

#by set subtraction (performance - 50 cycles in 65 sec)
def erastothenes_set(prime_range):
    main_array = [2] + list(range(3, prime_range, 2))
    i=3

    while i < math.sqrt(prime_range):
        to_subtr = set(range(2*i, prime_range, i))
        temp_set = set(main_array)
        main_array = list(temp_set - to_subtr)
        i = i + 1
    main_array.sort()
    return main_array


main_array = erastothenes_set(prime_range=104749)
    
print(f"Primes count: {len(main_array)}")
print(f"10001st prime number is: {main_array[-1]}")
