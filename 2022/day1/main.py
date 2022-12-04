from pathlib import Path
from functools import reduce
from heapq import nlargest

def read_input():
  input_file_path = Path(__file__).parent / 'input.txt'
  # input_file_path = Path(__file__).parent / 'test_input.txt'
  with open(input_file_path, 'r') as file:
    return file.read().splitlines()

# Generator to extract calories for each elf
def group_calories(input):
  out = []
  for calorie in input:
    if calorie == '':
      yield out
      out = []
    else:
      out.append(int(calorie))
  yield out

def main():
  input = read_input()
  elf_calories = list(group_calories(input))
  sum_elf_calories = [
    reduce(lambda x, y: x + y, elf_calorie)
      for elf_calorie in elf_calories
  ]
  print(f"Answer to task 1 is: {max(sum_elf_calories)}")
  print(f"Answer to task 2 is: {sum(nlargest(3, sum_elf_calories))}")

if __name__ == '__main__':
  main()
