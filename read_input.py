import os


def read_input_day1(file_path):
    left = []
    right =[]
    with open(file_path, 'r') as file:
        for line in file:
            #print(line)  # .strip() is used to remove any extra newline characters
            left.append(int(line.split('   ')[0]))
            right.append(int(line.split('   ')[1]))
        left.sort()
        right.sort()
        return left, right

left, right = read_input_day1("input/Day1_Part1.txt")


print(left)


diff = 0
for i in range(len(left)):
    diff += abs(right[i] - left[i])

print(diff)

for a,b in zip(left, right):
    diff += a-b

print(f'Total distance apart: {diff}')