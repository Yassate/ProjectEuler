import math

for a in range(1,1000):
    for b in range(1,1000):
        c = math.sqrt(a**2 + b**2)
        if a+b+c == 1000:
            print(f"a = {a}, b = {b}, c = {c}")
            print(f"Product = {a*b*c}")
            break


        
