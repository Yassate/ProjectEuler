palindromes = list()

def is_palindrome(numb):
    numb_string = str(numb)
    digit_count = len(numb_string)
    sep_digits = [x for x in numb_string]
    for i, digit in enumerate(sep_digits):
        if digit != sep_digits[digit_count-1-i]:
            return False
    return True


for i in reversed(range(100, 1000)):
    for j in reversed(range(100, 1000)):
        if is_palindrome(i*j):
            palindromes.append(i*j)

print(max(palindromes))
