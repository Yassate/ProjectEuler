import math

def get_div_count(number):
    div_count = 2
    calc_range = math.sqrt(number)
    if calc_range == int(calc_range):
        div_count = div_count - 1
    for div in range(2, int(calc_range) + 1):
        if number % div == 0:
            div_count = div_count + 2
    return div_count

def get_triangle_number(from_number):
    triangle = 0
    for i in range(1, from_number+1):
        triangle = triangle + i
    return triangle

def get_first_triangle_numbers(triangle_count):
    output_list = []
    for i in range(1, triangle_count):
        output_list.append(get_triangle_number(i))
    return output_list

triangle_numbers = get_first_triangle_numbers(15000)
highest = 0

for x in triangle_numbers:
    div_count = get_div_count(x)
    if div_count > 500:
        print(f"Triangle number: {x}, div count: {div_count}")
        break

