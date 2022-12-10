from math import sqrt
import operator
from pathlib import Path
from copy import copy

def read_input():
  input_file_path = Path(__file__).parent / 'input.txt'
  # input_file_path = Path(__file__).parent / 'example_input.txt'
  with open(input_file_path, 'r') as file:
    return file.read().splitlines()

def main():
  input = read_input()
  head_pos = [0, 0]
  tail_pos = [0, 0]
  visited_positions_unique = set() # Unordered unique elements

  for directions in input:
    direction = directions[0]
    steps = int(directions[2:])
    
    for _ in range(steps):
      match direction:
        case 'R': head_pos[0] += 1
        case 'L': head_pos[0] -= 1
        case 'U': head_pos[1] += 1
        case 'D': head_pos[1] -= 1

      diff = list(map(operator.sub, head_pos, tail_pos))

      if diff[0] > 1:
        tail_pos[0] += 1
      elif diff[0] < -1:
        tail_pos[0] -= 1
      elif diff[1] > 1:
        tail_pos[1] += 1
      elif diff[1] < -1:
        tail_pos[1] -= 1

      distance = sqrt((diff[0] * diff[0]) + (diff[1] * diff[1]))

      # If the head and tail aren't touching and aren't in the same row or column,
      # the tail always moves one step diagonally to keep up.
      if distance > 2.01:
        match direction:
          case 'U'|'D': tail_pos[0] = head_pos[0]
          case 'R'|'L': tail_pos[1] = head_pos[1]

      visited_positions_unique.add(tuple(tail_pos))
  
  # Draw map of visited positions for the tail, use offset
  # to move most negative position to (0, 0).
  offset_width = abs(min(elem[0] for elem in visited_positions_unique))
  offset_height = abs(min(elem[1] for elem in visited_positions_unique))
  map_width  = max(elem[0] for elem in visited_positions_unique) + 1 + offset_width
  map_height = max(elem[1] for elem in visited_positions_unique) + 2 + offset_height

  map_line = ['.' for _ in range(map_width)]
  trace_map = [copy(map_line) for _ in range(map_height) ]

  for line in visited_positions_unique:
    x = line[0] + offset_width
    y = line[1] + offset_height
    trace_map[y][x] = '#'
  trace_map[offset_height][offset_width] = 'S'

  # Rotate output 90 degree left to match example output
  for e in list(list(x) for x in zip(*trace_map))[::-1]:
    print(''.join(e))
  print()

  print(f"The answer to task 1 is: {len(visited_positions_unique)}")

if __name__ == '__main__':
  main()
