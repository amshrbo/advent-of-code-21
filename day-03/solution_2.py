'''
Results on test file are: 23*10 = 230
Results on input file are: 1459*3178 = 4636702
'''

data = []
with open('input.txt', 'r') as file:
    for line in file:
        data.append(line.strip())

def common_bit(data, idx, rate_type):
    '''
    finding the most or least common bit in a specific index 
    Input: 
        data: a list of digits.
        idx: the index in which i wann check the most common value in it.
    return:
        The common bit apears in this position.    
    '''

    #looping over to count the number of zeros
    zero_counter = 0
    for elem in data:
        for i, bit in enumerate(elem):         
            if i == idx and bit == '0':                
                zero_counter += 1

    if rate_type == 'oxygen':
        return '0' if zero_counter > (len(data) // 2) else '1'
    else:
        return '0' if zero_counter <= (len(data) // 2) else '1'


def data_filtering(data, bit_criteria, idx):
    '''
    Desc:
        filtering out the data based on the bit_criteria
    Input:
        data: list of values
        bit_criteria: 0 or 1 only keeping the similar bits
        idx: the index in which we are gonna filter
    return:
        remaining_data the filtered data based on the above conditions
    '''
    remaining_data = []

    for elem in data:
        for i, bit in enumerate(elem):         
            if i == idx:
                if bit == bit_criteria:
                    remaining_data.append(elem)
            else:
                continue
    
    return remaining_data
            

def calculate_rate(data, rate_type, idx=0):
    if len(data) == 1:
        return data
    else:
        bit_criteria = common_bit(data, idx, rate_type) 
        data = data_filtering(data, bit_criteria, idx)

        return calculate_rate(data, rate_type, idx=idx+1)


o2_rate = calculate_rate(data, rate_type='oxygen')
co2 = calculate_rate(data, rate_type='co2')
o2_decimal = int(o2_rate[0], 2)
co2_decimal = int(co2[0], 2)
life_support = o2_decimal * co2_decimal

print(o2_decimal, co2_decimal, life_support)
