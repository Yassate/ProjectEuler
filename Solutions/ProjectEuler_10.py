import math

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


main_array = erastothenes_set(prime_range=2000001)
    
print(f"Primes count: {len(main_array)}")
print(f"Last prime number is: {main_array[-1]}")
print(f"Sum of all primes in this range: {sum(main_array)}")
