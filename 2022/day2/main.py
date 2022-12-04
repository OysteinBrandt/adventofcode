from pathlib import Path
from enum import Flag, auto

def read_input():
  input_file_path = Path(__file__).parent / 'input.txt'
  # input_file_path = Path(__file__).parent / 'example_input.txt'
  with open(input_file_path, 'r') as file:
    return file.read().splitlines()

class HandShape(Flag):
  ROCK = auto()
  PAPER = auto()
  SCISSORS = auto()

def create_hand(player_input: str) -> HandShape:
  match player_input:
    case 'A' | 'X': return HandShape.ROCK
    case 'B' | 'Y': return HandShape.PAPER
    case 'C' | 'Z': return HandShape.SCISSORS
    case _: raise ValueError(f"Invalid input found: {player_input}")

def is_victory(you: HandShape, opponent: HandShape):
  match you:
    case HandShape.ROCK: return opponent == HandShape.SCISSORS
    case HandShape.SCISSORS: return opponent == HandShape.PAPER
    case HandShape.PAPER: return opponent == HandShape.ROCK
    case _: raise ValueError(f"Invalid input found: {you}")

def score_from_hand_selection(hand: HandShape) -> int:
  match hand:
    case HandShape.ROCK: return 1
    case HandShape.PAPER: return 2
    case HandShape.SCISSORS: return 3
    case _: raise ValueError(f"Invalid input found: {hand}")

def task1(input):
  total_score = 0
  for round in input:
    opponent = create_hand(round[0])
    you = create_hand(round[2])
    # print(opponent, you)
    is_draw = you == opponent
    if is_draw:
      score_for_outcome = 3
    elif is_victory(you, opponent):
      score_for_outcome = 6
    else:
      score_for_outcome = 0

    # print(f"Point from outcome: {score_for_outcome}")
    # print(f"Point from hand: {score_from_hand_selection(you)}")
    total_score += score_for_outcome + score_from_hand_selection(you)
  print(f"The answer to task 1 is: {total_score}")

############################################################################

def losing_hand_from(hand: HandShape) -> HandShape:
  match hand:
    case HandShape.ROCK: return HandShape.SCISSORS
    case HandShape.PAPER: return HandShape.ROCK
    case HandShape.SCISSORS: return HandShape.PAPER
    case _: raise ValueError(f"Invalid input found: {hand}")

def winning_hand_from(hand: HandShape) -> HandShape:
  match hand:
    case HandShape.ROCK: return HandShape.PAPER
    case HandShape.PAPER: return HandShape.SCISSORS
    case HandShape.SCISSORS: return HandShape.ROCK
    case _: raise ValueError(f"Invalid input found: {hand}")

# 2nd element in output is now the desired result of the battle
# X == lose
# Y == draw
# Z == win
def create_hand_from_desire(opponent: HandShape, desire: str) -> HandShape:
  match desire:
    case 'X': # Lose
      return losing_hand_from(opponent)
    case 'Z': # Win
      return winning_hand_from(opponent)
    case _: raise ValueError(f"Invalid input found: {desire}")

def task2(input):
  total_score = 0
  for round in input:
    opponent = create_hand(round[0])
    if round[2] == 'Y': # Draw
      you = opponent
    else:
      you = create_hand_from_desire(opponent, round[2])
    # print(f"Selected hand: {you}")

    is_draw = you == opponent
    if is_draw:
      score_for_outcome = 3
    elif is_victory(you, opponent):
      score_for_outcome = 6
    else:
      score_for_outcome = 0

    # print(f"Point from outcome: {score_for_outcome}")
    # print(f"Point from hand: {score_from_hand_selection(you)}")
    total_score += score_for_outcome + score_from_hand_selection(you)
  print(f"The answer to task 2 is: {total_score}")
    


############################################################################

def main():
  input = read_input()
  # print(input)

  task1(input)
  task2(input)

if __name__ == '__main__':
  main()
