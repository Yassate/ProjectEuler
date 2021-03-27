prev_number = 1
curr_number = 2
sum = 0
while(curr_number<4000000):
    if(curr_number%2 == 0):
        sum += curr_number
        
    temp_number = curr_number
    curr_number += prev_number
    prev_number = temp_number


print(sum)
    
