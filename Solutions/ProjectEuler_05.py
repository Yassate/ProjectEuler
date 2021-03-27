def divisible_by_20(number):
    for div in range(2,21):
        if number%div != 0:
            return False
    return True

number = 2520
while(True):
    if divisible_by_20(number):
        print(number)
        break
    number = number + 20
