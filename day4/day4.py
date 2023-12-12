file_name = "day4-inputs.txt"


def get_formatted_inputs(file_name):
    with open(file_name) as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def get_hands(line):
    [_, hands] = line.split(":")
    [hand1, hand2] = hands.split("|")
    
    return [hand1.split(), hand2.split()]


def calculate_score(winning_hand, player_hand):
    power = 0

    for i in range(0, len(player_hand)):
        if (player_hand[i] in winning_hand):
            power += 1
    
    if (power > 0):
        return 2**(power - 1)
    
    return 0


def run_program():
    points = 0

    games = get_formatted_inputs(file_name)
    for i in range(0, len(games)):
        hands = get_hands(games[i])
        points += calculate_score(hands[0], hands[1])
    
    return points
        

print("results: " + str(run_program()))
