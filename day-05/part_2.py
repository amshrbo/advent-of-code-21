import re
from pprint import pprint
import numpy as np
'''
Results of test should be: 5
Results of input should be: 
    
'''


def get_data(file):
    with open(file, 'r') as file:
        data = []
        maximum = 0
        for line in file.readlines():
            line = line.strip()
            if line:
                values = re.split(',|->', line)
                x1, y1, x2, y2 = values
                vent_line = [int(x1), int(y1), int(x2), int(y2)]
                if maximum < max(vent_line):
                    maximum = max(vent_line)

                data.append(vent_line)

    return data, maximum

def avoid_danger(lines, digram):
    num_overlaps = 0

    for line in lines:
        x1, y1, x2, y2 = line

        if x1 != x2 and y1 != y2: 
            # To determine Diagonal X1-X2 == y1-y2
            if abs(x1-x2) == abs(y1-y2): #Diagonal
                #diagonal                
                if x1 < x2:
                    # move from x1, y1 to x2, y2 by adding one on x sub one from y
                    counter = y1
                    for i in range(x1, x2+1):
                        digram[i, counter] += 1
                        counter -= 1
                else:
                    counter = y2
                    for i in range(x2, x1+1):
                        digram[i, counter] += 1
                        counter -= 1

        else:
            if x1 == x2:
                if y1 < y2:
                    for i in range(y1, y2+1):
                        digram[x1, i] += 1
                else:
                    for i in range(y2, y1+1):
                        digram[x1, i] += 1

            if y1 == y2:
                if x1 < x2:
                    for i in range(x1, x2+1):
                        digram[i, y1] += 1
                        
                else:
                    for i in range(x2, x1+1):
                        digram[i, y1] += 1
                # print(digram)

    # print(digram)
    for row in digram:
        for val in row:
            if val > 1:
                num_overlaps += 1

    return num_overlaps


def main():
    lines, maximum = get_data('input.txt')
    # pprint(lines)
    print(maximum)

    digram = np.zeros((maximum+1, maximum+1), dtype=int)

    # print(digram)

    overlaps = avoid_danger(lines, digram)
    print(overlaps)

if __name__ == '__main__':
    main()