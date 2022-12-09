from pathlib import Path
from typing import List

def read_input():
  input_file_path = Path(__file__).parent / 'input.txt'
  # input_file_path = Path(__file__).parent / 'example_input.txt'
  with open(input_file_path, 'r') as file:
    return file.read().splitlines()

def is_visible(tree_height: int, other_tree_heights: List[int]) -> bool:
  return not any(other_tree >= tree_height for other_tree in other_tree_heights)

def calculate_scenic_score(tree_height: int, other_tree_heights: List[int]) -> int:
  score = 0
  for other_tree in other_tree_heights:
    score += 1
    if other_tree >= tree_height:
      break
  return score

def main():
  input = read_input()
  width = len(input[0])
  height = len(input)
  visible_trees = 0
  best_scenic_score = 0
  for x in range(width):
    for y in range(height):
      tree = int(input[y][x])

      scenic_score = None
      # Trees on the edges are always visible
      if y == 0 or x == 0 or x == width-1 or y == height-1:
        visible_trees += 1
        scenic_score = 0 # Small optimization since all trees on edges will have a 0 distance
      else:
        # TODO: We could use generator expression here and in visible check because we are only iterating.
        if scenic_score is None:
          scenic_score_top = calculate_scenic_score(tree, reversed([int(input[i][x]) for i in range(y)]))
          scenic_score_bottom = calculate_scenic_score(tree, [int(input[i][x]) for i in range(y+1, height)])
          scenic_score_left = calculate_scenic_score(tree, reversed([int(input[y][i]) for i in range(x)]))
          scenic_score_right = calculate_scenic_score(tree, [int(input[y][i]) for i in range(x+1, width)])
          scenic_score = scenic_score_top * scenic_score_bottom * scenic_score_left * scenic_score_right

        if scenic_score > best_scenic_score:
          best_scenic_score = scenic_score

        # TODO:
        # We could check the entire range of x (left to right) in one statement,
        # and then the entire y (top to bottom) in one statement,
        # we would then have to exclude the "current tree" from the search range
        if not is_visible(tree, [int(input[i][x]) for i in range(y)]):                 # top
          if not is_visible(tree, [int(input[i][x]) for i in range(y+1, height)]):     # bottom
            if not is_visible(tree, [int(input[y][i]) for i in range(x)]):             # left
              if not is_visible(tree, [int(input[y][i]) for i in range(x+1, width)]):  # right
                continue
        visible_trees += 1

  print(f"The answer to task 1 is: {visible_trees}")
  print(f"The answer to task 2 is: {best_scenic_score}")

if __name__ == '__main__':
  main()
