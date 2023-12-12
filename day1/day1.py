import re
file_name = "day1-inputs.txt"

# Get formatted inputs from file
def get_formatted_inputs(file_name):
    with open(file_name) as f:
        lines = f.readlines()

    return [line.strip() for line in lines]

def get_sum(values):
    sum = 0

    for i in range(0, len(values)):
        sum += values[i]

    return sum

def get_digit(number_string):
    if (number_string == 'one'):
        return 1
    elif (number_string == 'two'):
        return 2
    elif (number_string == 'three'):
        return 3
    elif (number_string == 'four'):
        return 4
    elif (number_string == 'five'):
        return 5
    elif (number_string == 'six'):
        return 6
    elif (number_string == 'seven'):
        return 7
    elif (number_string == 'eight'):
        return 8
    elif (number_string == 'nine'):
        return 9
    else:
        return number_string
        
        

def find_first_and_last_number(random_string):
    regex_string = r'\d|one|two|three|four|five|six|seven|eight|nine'
    [first, last] = [re.findall(regex_string, random_string)[0], re.findall(regex_string, random_string)[-1]] 

    return str(get_digit(first)) + str(get_digit(last))


def run_program():
    lines = get_formatted_inputs(file_name);
    numbers = []
    
    for i in range(0, len(lines)):
        numbers.append(int(find_first_and_last_number(lines[i])))

    return get_sum(numbers)


print("result: " + str(run_program()))