import random
list = []

with open('input.txt', 'w') as f_in:
    for i in range(3):
            x = random.randint(1,10)
            f_in.write(str(x))
            f_in.write('\n')

with open('input.txt') as f_in, open('output.txt', 'w') as f_out:
    for line in f_in:
        for i in range(int(line)):
            f_out.write("X")
        f_out.write('\n')
