from enum import Enum


class RPS(Enum):

    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'


ELF_RPS = {
    'A': RPS.ROCK,
    'B': RPS.PAPER,
    'C': RPS.SCISSORS,
}


HUMAN_RPS = {
    'X': RPS.ROCK,
    'Y': RPS.PAPER,
    'Z': RPS.SCISSORS,
}


WIN_LOGIC = {
    RPS.ROCK: RPS.SCISSORS,
    RPS.PAPER: RPS.ROCK,
    RPS.SCISSORS: RPS.PAPER
}


RPS_SCORE = {
    RPS.ROCK: 1 ,
    RPS.PAPER: 2,
    RPS.SCISSORS: 3,
}


DRAW_SCORE = 3
WIN_SCORE = 6

with open('input_data.txt', 'r') as infile:
    input_data: list = infile.read().splitlines()

def evaluate_game(player_choice: RPS, opponent_choice: RPS) -> int:
    choice_score = RPS_SCORE[player_choice]
    outcome_score = 0
    if player_choice == opponent_choice:
        outcome_score = 3
    elif WIN_LOGIC[player_choice] == opponent_choice:
        outcome_score = 6
    return choice_score + outcome_score

tournament_score = 0
for game in input_data:
    elf_encoded_choice, human_encoded_choice = game.split(' ')
    elf_choice = ELF_RPS[elf_encoded_choice]
    human_choice = HUMAN_RPS[human_encoded_choice]
    game_score = evaluate_game(human_choice, elf_choice)
    tournament_score += game_score


print(tournament_score)
