import re
file_name = "day2-inputs.txt"

max_number_by_cube_color = {"blue": 14, "green": 13, "red": 12};
# Get formatted inputs from file
def get_formatted_inputs(file_name):
    with open(file_name) as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def calculate_highest_number_by_cube(grab):
    highest_numbers_by_cube = {"blue": 0, "green": 0, "red": 0};
    grabs = grab.split(";")
    for i in range(0, len(grabs)):
        cube = grabs[i].split(",")
        for j in range(0, len(cube)):
          color = cube[j].strip().split(" ")[1]
          number = int(cube[j].strip().split(" ")[0])

          if (color == "blue"):
              if (number > highest_numbers_by_cube["blue"]):
                  highest_numbers_by_cube["blue"] = number
          elif (color == "green"):
              if (number > highest_numbers_by_cube["green"]):
                  highest_numbers_by_cube["green"] = number
          elif (color == "red"):
              if (number > highest_numbers_by_cube["red"]):
                  highest_numbers_by_cube["red"] = number

    return highest_numbers_by_cube


def format_games(games):
    formatted_games = []

    for i in range(0, len(games)):
        [game_info, game_data] = games[i].split(":")
        index = re.findall(r'\d+', game_info)[0];
                  
        formatted_games.append({index: calculate_highest_number_by_cube(game_data)})

    return formatted_games


def get_game_power(game):
    for key in game:
        return game[key]["blue"] * game[key]["green"] * game[key]["red"]


def get_sum(values):
    sum = 0

    for i in range(0, len(values)):
        sum += values[i]

    return sum


def play_game1():
    games = format_games(get_formatted_inputs(file_name));
    valid_games = []

    for i in range(0, len(games)):
        game = games[i]
        for key in game:
            if (game[key]["blue"] <= max_number_by_cube_color["blue"] and game[key]["green"] <= max_number_by_cube_color["green"] and game[key]["red"] <= max_number_by_cube_color["red"]):
                valid_games.append(int(key))
    
    return get_sum(valid_games)

def play_game2():
    games = format_games(get_formatted_inputs(file_name));
    game_powers = []

    for i in range(0, len(games)):
        game_powers.append(get_game_power(games[i]))
        
    
    return get_sum(game_powers)


print("part 1 result: " + str(play_game1()))
print("part 2 result: " + str(play_game2()))