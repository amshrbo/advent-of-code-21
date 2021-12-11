## ouput of the test file = 60*15

horisontal = 0
depth = 0
aim = 0

with open('./input.txt', 'r') as file:
    for line in file:
        try:
            key_word, value = line.split(' ')
            value = int(value)
        except Exception as e:
            print('blank line')
            break
        
        if key_word == 'forward':
            horisontal += value
            depth += aim * value

        elif key_word == 'down':
            aim += value            
        else:
            aim -= value

print(depth, horisontal, depth*horisontal)    