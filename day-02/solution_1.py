## ouput of the test file = 144

horisontal = 0
depth = 0

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

        elif key_word == 'down':
            depth += value
        else:
            depth -= value

print(depth, horisontal, depth*horisontal)    