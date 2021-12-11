"""
Results in test should be: 198
Results in input should be: 845186

bits_len -> 12 in input, 5 in test
"""

gamma = ''
epsilon = ''
bits_len = 12 # change to `5` in test
lst_dict = [{'zeros': 0, 'ones': 0} for _ in range(bits_len)]

with open('./input.txt', 'r') as file:
    for line in file:
        for idx, digit in enumerate(line.strip()):
            if digit == '0':
                lst_dict[idx]['zeros'] += 1
            else:
                lst_dict[idx]['ones'] += 1


for digit in lst_dict:
    if digit['zeros'] > digit['ones']:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(int(gamma, 2) * int(epsilon, 2))