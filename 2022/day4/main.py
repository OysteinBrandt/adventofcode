from pathlib import Path

def read_input():
  input_file_path = Path(__file__).parent / 'input.txt'
  # input_file_path = Path(__file__).parent / 'example_input.txt'
  with open(input_file_path, 'r') as file:
    return file.read().splitlines()

def main():
  input = read_input()

  num_pairs_contained_in_other = 0
  num_pairs_overlap = 0
  for assignment_pairs in input:
    first_section, second_section = assignment_pairs.split(',')
    first_start, first_end = (int(x) for x in first_section.split('-'))
    second_start, second_end = (int(x) for x in second_section.split('-'))

    if (first_start >= second_start and first_end <= second_end) or \
       (second_start >= first_start and second_end <= first_end):
      num_pairs_contained_in_other += 1

    if (first_start <= second_end and second_start <= first_end):
      num_pairs_overlap += 1

  print(f"Answer to task 1 is: {num_pairs_contained_in_other}")
  print(f"Answer to task 2 is: {num_pairs_overlap}")

if __name__ == '__main__':
  main()
