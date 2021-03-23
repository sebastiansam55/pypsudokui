#!/usr/bin/python3

import json

def check_consecutive(l: list):
    """
    Check if l has one of 1-9.
    Assumes l in appropriate size.
    Quick checks via sum, then list comparison.
    """
    onetonine = [1,2,3,4,5,6,7,8,9]
    if sum(l) != 45:
        return False
    l.sort()
    elif onetonine == l:
        # print("valid section 1-9")
        return True

def get_grid(grid, x, y):
    """
    Returns a mini 3x3 grid corresponding to the xy coords given
    Starts in upper left hand corner
    """
    grid = grid[x*3:(x+1)*3]
    for count,line in enumerate(grid):
        grid[count] = line[y*3:(y+1)*3]
    return grid

def check_super_grid(grid):
    """
    Check each mini grid in 9x9 sudoku grid for validity.
    Does not check rows or columns.
    """
    valid_grid = 0
    for x in range(0,3):
        for y in range(0,3):
            mini_grid = get_grid(grid, x,y)
            if check_grid(mini_grid):
                valid_grid += 1
                pass
            else:
                if valid_grid>3:
                    print("Valid grids before fail", valid_grid)
                return False
    return True

def check_grid(grid):
    """
    Takes 2d array of form [[1,2,3],[4,5,6],[7,8,9]]
    Checks if digits 1-9 are there
    """
    return check_consecutive([j for i in grid for j in i])

def mk_grid(l: str):
    """
    Makes sudoku grid object give a 81 (9x9) length string.
    Assumes string is the correct size.
    """
    ret_list = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ]
    for line_count,i in enumerate(range(0,81,9)):
        line = l[i:i+9]
        for pos, c in enumerate(line):
            ret_list[line_count][pos] = int(c)

    return ret_list


with open('pydigits.json', 'r') as f:
    # load in data, slower way but it is front loaded so no big deal
    d = ""
    for line in f:
        if len(line)<10:
            break
        data = json.loads(line.strip())
        d+=data['content']

    for count,digit in enumerate(range(81,len(d))):
        l = d[digit-81:digit]
        grid = mk_grid(l)
        fail = False
        #check each line for consecutive digits
        for line in grid:
            fail = not check_consecutive(line)
            if fail: break
        if count % 10000 == 0: print("Failed grids: ", count)
        if fail: continue
        #this did not fire within the first 10 million digits.
        print("All lines good")
        #if all lines are good check grid.
        if check_super_grid(grid):
            print("Found!")
            print(grid)
            print(digit)
            print(l)
        #TODO if this condition is ever reached the columns
        # should also be checked.
        break

