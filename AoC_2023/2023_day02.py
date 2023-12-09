#solution for Day 2 problem

data = open(r"C:\Users\swati\Kushagra\Temp\AoC2023\Input2_1.txt", "r+")

thresholds = {"red": 12, "green": 13, "blue": 14}
possibles = 0

for line in data:
    game_info, sets = line.split(": ")
    groups = map(str.split, sets.replace(";", ",").split(", "))
    # print(list(groups))
    if all(int(cube_nums) <= thresholds[cube_color] for cube_nums, cube_color in groups):
        possibles += int(game_info.split(" ")[1])
        
print(possibles)