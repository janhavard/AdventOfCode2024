import os


def read_input_day2(file_path):
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
