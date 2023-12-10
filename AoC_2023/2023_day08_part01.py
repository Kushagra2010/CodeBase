
import time
st = time.time()

input_data = open(r"C:\Users\swati\Kushagra\Temp\AoC2023\input.txt","r+")

directions = input_data.readline().strip()
puzzle_data = input_data.readlines()[1:]

#Solution 1
for x in puzzle_data:
    puzzle_map= {x.split(' = ')[0]:x.split(' = ')[1] for x in puzzle_data}
    
steps1 = 0
# curr_pos = puzzle_data[0][:4].strip()
curr_pos = '??A'
break_loop=1

while (break_loop):
    for direction in directions:
        if curr_pos =='ZZZ':
            break_loop = 0
            break
        if direction == 'L':
            curr_pos = puzzle_map[curr_pos.strip()].split(',')[0].replace('(','').strip()
        else:
            curr_pos = puzzle_map[curr_pos.strip()].split(',')[1].replace(')','').strip()
        steps1 +=1
        
print('Answer for 1st puzzle: ',steps1)
