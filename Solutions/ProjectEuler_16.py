def sum_of(number):
    sum = 0
    digits = [int(x) for x in str(number)]
    for digit in digits:
        sum = sum + digit
    return sum

print(sum_of(2**1000))
