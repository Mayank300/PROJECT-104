# ----------------- common -----------------

import csv
from collections import Counter 

with open('SOCR-HeightWeight.csv', newline = '') as f:

    reader = csv.reader(f)

    file_data = list(reader)

    file_data.pop(0)
    file_data.pop(1)
    
    new_data = []

    for i in range(len(file_data)):
        n_num = file_data[i][2]

        new_data.append(float(n_num))


# xxxxxxxxxxxxxxxxx common xxxxxxxxxxxxxxxxx

# ----------------- mean -----------------

    num = len(new_data)

    total = 0

    for x in new_data:
        total += x

    mean = total/num

# xxxxxxxxxxxxxxxxx mean xxxxxxxxxxxxxxxxx
    


# ----------------- median -----------------

    new_data.sort()

    if num % 2 == 0:
        median_1 = float(new_data[num // 2])
        median_2 = float(new_data[num // 2 + 1])

        median = (median_1 + median_2) / 2

    else:
        median = float(new_data[num // 2])



# xxxxxxxxxxxxxxxxx median xxxxxxxxxxxxxxxxx

# ----------------- mode -----------------

    data = Counter(new_data)

    mode_data = {
        "75-85" : 0,
        "85-95" : 0,
        "95-105" : 0,
        "105-115" : 0,
        "115-125" : 0,
        "125-135" : 0,
        "135-145" : 0,
        "145-155" : 0,
        "155-165" : 0,
        "165-175" : 0,
    }

    for h,o in data.items():
        if 75 < float(h) < 85:
            mode_data['75-85']+= o

        elif 85 < float(h) < 95:
            mode_data['85-95']+= o

        elif 95 < float(h) < 105:
            mode_data['95-105']+= o
               
        elif 105 < float(h) < 115:
            mode_data['105-115']+= o

        elif 115 < float(h) < 125:
            mode_data['115-125']+= o

        elif 125 < float(h) < 135:
            mode_data['125-135']+= o

        elif 135 < float(h) < 145:
            mode_data['135-145']+= o

        elif 145 < float(h) < 155:
            mode_data['145-155']+= o

        elif 155 < float(h) < 165:
            mode_data['155-165']+= o

        elif 165 < float(h) < 175:
            mode_data['165-175']+= o

    mode_range, mode_occurences = 0,0

    for range, occurences in mode_data.items():
        if occurences > mode_occurences:
            mode_range, mode_occurences = [int(range.split("-")[0]), int(range.split("-")[1])], occurences
    mode = float((mode_range[0] + mode_range[1]) / 2)

    mode = float((mode_range[0]+mode_range[1])/2)

# xxxxxxxxxxxxxxxxx mode xxxxxxxxxxxxxxxxx



#  ----------------- print -----------------

print("Mean (Average) is -> ", mean)
print("Median is is -> ", median)
print("Mode is is -> ",  mode)

# xxxxxxxxxxxxxxxxx print xxxxxxxxxxxxxxxxx

