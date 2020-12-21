"""
TO DO
1. Extend each line (x35?)
2. Depending on each line number, the target will be at a different position.
2a. Line 0, index 0. Line 1, index 3. Line 2, index 6.
3. Is target a tree? Check if #. Add to counter.

# 324 lines
# 31 characters per line
"""

# Grab input data
f = open('input.txt', 'r')
slope = f.read()
slope = slope.split('\n')

# Clean data: extend lines, remove empty lines
slope_extended = []
for line in slope:
    if line == '':
        slope.remove(line)
    else:
        slope_extended.append(line*100)

# First problem
def toboggan_trajectory(traverse):
    tree_count = 0
    for count,line in enumerate(slope_extended):
        if line[count*traverse] == '#':
            tree_count += 1

    print(tree_count)

# toboggan_trajectory(3)

# Second problem
def toboggan_trajectory2(*args):
    tree_list = []
    slope_extended_abridged = []


    for arg in args:
        tree_count = 0
        if arg[1] == 1:
            for count,line in enumerate(slope_extended):
                if line[count*arg[0]] == '#':
                    tree_count += 1
            tree_list.append(tree_count)
        # elif arg[1] == 2:
        #     for count,line in enumerate(slope_extended):
        #         if count % 2 == 0:
        #             if line[count*arg[0]] == '#':
        #                 tree_count += 1
        #     tree_list.append(tree_count)
        elif arg[1] == 2:
            for count,line in enumerate(slope_extended):
                if count % 2 == 0:
                    slope_extended_abridged.append(line)
            for count,line in enumerate(slope_extended_abridged):
                if line[count*arg[0]] == '#':
                    tree_count += 1
            tree_list.append(tree_count)
                
    print(tree_list)
            
    
    total = 1
    for t in tree_list:
        total *= t
    print(total)

toboggan_trajectory2((1,1),(3,1),(5,1),(7,1),(1,2))