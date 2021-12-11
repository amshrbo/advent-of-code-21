# reading the input as array of ints
def read_as_array(file_name):
    content = []
    with open(file_name, 'r') as file:
        for line in file:
            content.append(int(line.strip()))

    return content


content = read_as_array('../input.txt')

increasing_cnt = 0
previous = content[0]

for item in content[1:]:
    if item > previous:
        increasing_cnt += 1

    previous = item

print(increasing_cnt)