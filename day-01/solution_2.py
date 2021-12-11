# reading the input as array of ints
def read_as_array(file_name):
    content = []
    with open(file_name, 'r') as file:
        for line in file:
            content.append(int(line.strip()))

    return content

input_file = '../input.txt'


content = read_as_array(input_file)

a, b, c, = content[0], content[1], content[2]
sum = a + b + c
prev_sum = None
increasing_cnt = 0

for item in content[3:]:
    if prev_sum == None:
        prev_sum = sum
    
    a = b
    b = c
    c = item
    sum = a + b + c

    if sum > prev_sum:
        increasing_cnt += 1
    
    prev_sum = sum
    

print(increasing_cnt)



