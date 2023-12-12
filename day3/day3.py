import re
file_name = "day3-inputs.txt"

# Fix: Currently only checks for first digit in number

# Get formatted inputs from file
def get_formatted_inputs(file_name):
    with open(file_name) as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def build_grid(lines):
    grid = []

    for i in range(0, len(lines)):
    
        grid.append([*lines[i]])
        
    return grid


def is_digit(n):
    if (re.match(r'\d', n)):
        return True
    

def has_adjacent_symbol_horizontal(row, i):
    j = i - 1
    k = i + 1

    if (j >= 0 and row[j] != "." and not is_digit(row[j])):
        return True

    if (k < len(row) and row[k] != "." and not is_digit(row[k])):
        return True

    return False
        

def has_adjacent_symbol_vertical(grid, i, j):
    k = i - 1
    l = i + 1

    if (k >= 0 and grid[k][j] != "." and not is_digit(grid[k][j])):
        return True

    if (l < len(grid) and grid[l][j] != "." and not is_digit(grid[l][j])):
        return True

    return False


def has_adjacent_symbol_diagonal(grid, i, j):
    k = i - 1
    m = j - 1
    
    if (k >= 0 and m >= 0 and grid[k][m] != "." and not is_digit(grid[k][m])):
         return True
        
    k = i - 1
    m = j + 1

    if (k >= 0 and m < len(grid[k]) and grid[k][m] != "." and not is_digit(grid[k][m])):
        return True

    k = i + 1
    m = j + 1

    if (k < len(grid) and m < len(grid[k]) and grid[k][m] != "." and not is_digit(grid[k][m])):
        return True

    k = i + 1
    m = j - 1

    if (k < len(grid) and m >= 0 and grid[k][m] != "." and not is_digit(grid[k][m])):
        return True
        
    return False
    

def is_adjacent_to_symbol(grid, i, j):
    if (has_adjacent_symbol_horizontal(grid[i], j) or has_adjacent_symbol_vertical(grid, i, j) or has_adjacent_symbol_diagonal(grid, i, j )):
        return True
    else:
        return False
    

def get_whole_number(row, i):
    number = ""
    j = i
    k = i - 1

    while j < len(row):
        if (is_digit(row[j])):
            number += row[j]
            j += 1
        else:
            break

    while k >= 0:
        if (is_digit(row[k])):
            number = row[k] + number
            k -= 1
        else:
            break
                
    return [number, j - i]
    

def get_gear_ratio(numbers):
    return numbers[0] * numbers[1]
 

def get_adjacent_numbers(grid, i, j):
    numbers = []
    top_adjacent = False
    bottom_adjacent = False

    # horizontal
    if (is_digit(grid[i][j+1])):
        [number, _] = get_whole_number(grid[i], j+1)
        numbers.append(int(number))
    
    if (is_digit(grid[i][j-1])):
        [number, _] = get_whole_number(grid[i], j-1)
        numbers.append(int(number))

    # vertical
    if (is_digit(grid[i+1][j])):
        bottom_adjacent = True
        [number, _] = get_whole_number(grid[i+1], j)
        numbers.append(int(number))

    if (is_digit(grid[i-1][j])):
        top_adjacent = True
        [number, _] = get_whole_number(grid[i-1], j)
        numbers.append(int(number))

    # diagonal
    if (not bottom_adjacent and is_digit(grid[i+1][j+1])):
        [number, _] = get_whole_number(grid[i+1], j+1)
        numbers.append(int(number))

    if (not top_adjacent and is_digit(grid[i-1][j-1])):
        [number, _] = get_whole_number(grid[i-1], j-1)
        numbers.append(int(number))

    if (not bottom_adjacent and is_digit(grid[i+1][j-1])):
        [number, _] = get_whole_number(grid[i+1], j-1)
        numbers.append(int(number))

    if (not top_adjacent and is_digit(grid[i-1][j+1])):
        [number, _] = get_whole_number(grid[i-1], j+1)
        numbers.append(int(number))

    return numbers


def find_parts_number(grid):
    valid_numbers = []

    for i in range(0, len(grid)):
        j = 0
        while j < len(grid[i]):
            if (is_digit(grid[i][j]) ):
                [number, lengthToEndOfNumber] = get_whole_number(grid[i], j)
                if (is_adjacent_to_symbol(grid, i, j)):
                    valid_numbers.append(int(number))
                    j += lengthToEndOfNumber
                else:
                    j += 1
            else:
                j += 1
                
    return valid_numbers


def find_gear_ratios(grid):
    valid_gear_ratios = []

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (grid[i][j] == "*" ):
                numbers = get_adjacent_numbers(grid, i, j)
                if (numbers and len(numbers) == 2):
                    valid_gear_ratios.append(get_gear_ratio(numbers))

    return valid_gear_ratios


def get_sum(values):
    sum = 0

    for i in range(0, len(values)):
        sum += values[i]

    return sum


def run_program():
    return get_sum(find_parts_number(build_grid(get_formatted_inputs(file_name))))

def run_program2():
    return get_sum(find_gear_ratios(build_grid(get_formatted_inputs(file_name))))

print("result: ", run_program())
print("result2: ", run_program2())