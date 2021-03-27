def sum_of_powers(number):
    sum = 0
    for i in range(1, number+1):
        sum = sum + i ** 2
    return sum

def power_of_sum(number):
    return ((1+number)/2*number)**2

print(power_of_sum(100) - sum_of_powers(100))
