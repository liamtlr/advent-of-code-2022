from enum import Enum


class RPS(Enum):

    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'

class Outcomes(Enum):

    LOSE = 'X'
    DRAW = 'Y'
    WIN = 'Z'


ELF_RPS = {
    'A': RPS.ROCK,
    'B': RPS.PAPER,
    'C': RPS.SCISSORS,
}


WIN_LOGIC = {
    RPS.ROCK: RPS.SCISSORS,
    RPS.PAPER: RPS.ROCK,
    RPS.SCISSORS: RPS.PAPER
}


LOSE_LOGIC = {
    RPS.SCISSORS: RPS.ROCK,
    RPS.ROCK: RPS.PAPER,
    RPS.PAPER: RPS.SCISSORS,
}


RPS_SCORE = {
    RPS.ROCK: 1 ,
    RPS.PAPER: 2,
    RPS.SCISSORS: 3,
}


OUTCOME_SCORE = {
    Outcomes.WIN.value: 6,
    Outcomes.LOSE.value: 0,
    Outcomes.DRAW.value: 3,

}


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

def get_corresponding_choice(opponent_choice: RPS, outcome: Outcomes) -> RPS:
    if outcome == Outcomes.WIN.value:
        return LOSE_LOGIC[opponent_choice]
    elif outcome == Outcomes.LOSE.value:
        return WIN_LOGIC[opponent_choice]
    return opponent_choice

tournament_score = 0
for game in input_data:
    elf_encoded_choice, outcome = game.split(' ')
    elf_choice = ELF_RPS[elf_encoded_choice]
    outcome_score = OUTCOME_SCORE[outcome]
    choice = get_corresponding_choice(elf_choice, outcome)
    choice_score = RPS_SCORE[choice]
    tournament_score += (outcome_score + choice_score)

print(tournament_score)
