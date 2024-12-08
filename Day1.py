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

left, right = read_input_day1("input/Day1.txt")

diff = 0
for a,b in zip(left, right):
    diff += a-b

print(f'Total distance apart: {diff}')

similarity_score = 0
for i in range(len(left)):
    if right.count(left[i]) > 0:
        similarity_score += left[i]*right.count(left[i])

print(f'Similarity score is: {similarity_score}')
