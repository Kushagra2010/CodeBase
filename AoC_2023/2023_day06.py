input_data = "Time:        58     99     64     69\nDistance:   478   2232   1019   1071".strip()
# input_data = "Time:      7  15   30\nDistance:  9  40  200"
input_data=input_data.split('\n')
t,d = input_data
times = [int(x) for x in t.split(': ')[1].split()]
dist = [int(x) for x in d.split(': ')[1].split()]

i=0
ans = 1
# distance=0
for time in times:
    number_ways=0
    for speed in range(1,time):
        distance = speed*(time-speed)
        if distance >dist[i]:
            number_ways+=1
    ans*=number_ways
    i+=1
print(ans)

================

import time
st = time.time()
input_data = "Time:        58     99     64     69\nDistance:   478   2232   1019   1071".strip()
# input_data = "Time:      7  15   30\nDistance:  9  40  200"
input_data=input_data.split('\n')
t,d = input_data
times = [str(x) for x in t.split(': ')[1].split()]
dist = [str(x) for x in d.split(': ')[1].split()]

race_time=''
lastdistance=''
number_ways=0
for x in times:
    race_time+=x
race_time = int(race_time)
    
for x in dist:
    lastdistance+=x
lastdistance = int(lastdistance)

for speed in range(1,race_time):
    distance = speed*(race_time-speed)
    if distance >lastdistance:
        number_ways+=1

print(number_ways)
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
