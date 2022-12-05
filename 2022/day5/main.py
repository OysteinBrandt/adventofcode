from pathlib import Path
import re, copy

def read_input():
  input_file_path = Path(__file__).parent / 'input.txt'
  # input_file_path = Path(__file__).parent / 'example_input.txt'
  with open(input_file_path, 'r') as file:
    return file.read().splitlines()

def main():
  input = read_input()

  num_stacks = (len(input[0]) + 1) // 4
  stacks = [[] for _ in range(num_stacks)]
  moves = []
  re_pattern_moves = re.compile(r"\d+")
  for line in input:
    if not line: continue

    if '[' in line:
      for i in range(1, len(line), 4):
        if line[i] == ' ':
          continue
        else:
          stack_idx = ((i + 3) // 4) - 1
          stacks[stack_idx].append(line[i])
    elif line.startswith('move'):
      moves.append([int(x) for x in re_pattern_moves.findall(line)])

  for stack in stacks:
    stack.reverse()

  task_2_stacks = copy.deepcopy(stacks)

  # Task 1
  for _num, _from, _to in moves:
    for _ in range(_num):
      stacks[_to-1].append(stacks[_from-1].pop())

  crates_on_top = "".join([x.pop() for x in stacks])
  print(f"The answer to task1 is: {crates_on_top}")

  # Task 2 - aka. CrateMover 9001
  for _num, _from, _to in moves:
    _from -= 1
    _to -= 1
    task_2_stacks[_to].extend(task_2_stacks[_from][len(task_2_stacks[_from]) - _num:])
    del task_2_stacks[_from][len(task_2_stacks[_from]) - _num:]

  crates_on_top = "".join([x.pop() for x in task_2_stacks])
  print(f"The answer to task2 is: {crates_on_top}")

if __name__ == '__main__':
  main()
