import csv

with open('SOCR-HeightWeight.csv', newline = '') as f:

    reader = csv.reader(f)

    file_data = list(reader)

    file_data.pop(0)
    file_data.pop(1)

    new_data = []

    for i in range(len(file_data)):
        n_num = file_data[i][2]

        new_data.append(float(n_num))

    num = len(new_data)
    
    new_data.sort()

    if num % 2 == 0:
        median_1 = float(new_data[num // 2])
        median_2 = float(new_data[num // 2 + 1])

        median = (median_1 + median_2) / 2

    else:
        median = float(new_data[num // 2])


print(median)