

def read_input():
    lines = []
    with open('input/Day4.txt', 'r') as file:
        for line in file:
            lines.append(line)
    return lines

def count_XMAS(lines):
    total_count = 0
    for row in range(len(lines)):
        for position in range(len(lines[row]) - 3):
            total_count += check_horizontal(lines, row, position)
    for row in range(len(lines) - 3):
        for position in range(len(lines[row])):
            total_count += check_vertical(lines, row, position)
    for row in range(len(lines) - 3):
        for position in range(len(lines[row]) - 3):
            total_count += check_diagonal(lines, row, position)
    for row in range(len(lines) - 3):
        for position in range(len(lines[row]) - 3):
            total_count += check_back_diagonal(lines, row, position)
    return total_count

def check_vertical(lines, row, position):
    vertical = ''.join([lines[i][position] for i in range(row, row+4)])
    return check_if_word_is_xmas(vertical)

def check_horizontal(lines, row, position):
    horizontal = lines[row][position:position+4]
    return check_if_word_is_xmas(horizontal)

def check_diagonal(lines, row, position):
    diagonal = lines[row][position]+lines[row+1][position+1]+lines[row+2][position+2] + lines[row+3][position+3]
    return check_if_word_is_xmas(diagonal)

def check_back_diagonal(lines, row, position):
    diagonal = lines[row][position+3] + lines[row+1][position+2] + lines[row+2][position+1] + lines[row+3][position]
    return check_if_word_is_xmas(diagonal)

def check_if_word_is_xmas(word):
    if word == 'XMAS' or word == 'SAMX':
        return 1
    return 0


lines = read_input()
print(f'Total number of XMAS: {count_XMAS(lines)}')