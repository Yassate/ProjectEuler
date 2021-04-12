def count_letters(number):
    
    tens_count = {0:0, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
    under_twenty = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3,
                         11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
    
    hundreds = int(number/100)
    under_100 = number%100
    if under_100>19:
        tens = int(under_100/10)
        digits = number%10
    else:
        tens = 0
        digits = under_100

    count = under_twenty[hundreds] + tens_count[tens] + under_twenty[digits]
    if number > 99:
        count = count + 10 #'hundred and'
    if number%100 == 0:
        count = count - 3 #'and'

    return count

overall_count = 0

for i in range(1, 1000):
    overall_count = overall_count + count_letters(i)

print(overall_count + len("onethousand"))
