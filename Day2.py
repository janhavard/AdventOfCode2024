import os


def read_input(file_path):
    reports = []
    with open(file_path, 'r') as file:
        for line in file:
            #print(line)  # .strip() is used to remove any extra newline characters
            reports.append([int(x) for x in line.split(' ')])
    return reports

def is_report_valid(report):
    for i in range(len(report)-1):
        diff = report[i+1] - report[i]
        if abs(diff) < 1 or abs(diff) > 3: #Check step size validity
            return False
        if i > 0: #Check constant sign through report
            previous_sign = report[i] - report[i-1]
            current_sign = report[i+1] - report[i]
            if previous_sign/current_sign < 0:
                return False
    return True

def count_valid_reports(reports):
    valid_reports = 0
    for i in range(len(reports)):
        if is_report_valid(reports[i]):
            valid_reports += 1
    return valid_reports



reports = read_input('input/Day2.txt')
valid_reports = count_valid_reports(reports, 1)
print(f'Number of valid reports: {valid_reports}')

