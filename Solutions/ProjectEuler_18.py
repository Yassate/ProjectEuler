def parse_to_list(to_parse):
    levels = list()
    for level in to_parse.split('\n'):
        levels.append(level.split(' '))
    return levels
       
def bit_sequence_from_number(number):
    s = bin(number)
    return list(s[2:].zfill(15))

def traverse(graph, sequence):
    sum1 = 0
    cur_offset = 0
    for level, direction in enumerate(sequence):
        cur_offset = int(direction) + cur_offset
        sum1 = sum1 + int(graph[level][cur_offset])
    return sum1
        
triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

#BRUTE FORCE
routes = 2**14
maximum = 0
graph = parse_to_list(triangle)

for route in range(routes):
    sequence = bit_sequence_from_number(route)
    cur_sum = traverse(graph, sequence)
    maximum = cur_sum if cur_sum>maximum else maximum

print(maximum)
