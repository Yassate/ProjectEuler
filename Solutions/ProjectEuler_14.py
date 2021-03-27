def is_even(number):
    return number%2 == 0

def next_Collatz(number):
    if is_even(number):
        return number/2
    else:
        return 3 * number + 1

def check_number(start):
    sequence = []
    last_numb = start
    next_numb = 0
    while next_numb != 1:
        next_numb = next_Collatz(last_numb)
        sequence.append(next_numb)
        last_numb = next_numb
    return [start, len(sequence)]

highest = [1, 1]
for i in range(1, 1000000):
    res = check_number(i)
    if(res[1] > highest[1]):
        highest = res

print(highest)
