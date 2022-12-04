from pathlib import Path
import string

def read_input():
  input_file_path = Path(__file__).parent / 'input.txt'
  # input_file_path = Path(__file__).parent / 'example_input.txt'
  with open(input_file_path, 'r') as file:
    return file.read().splitlines()

def main():
  input = read_input()
  # print(input)

  priority_lower = dict(
    zip(
      string.ascii_lowercase,
      range(1, len(string.ascii_lowercase) + 1),
      strict=True)
  )
  priority_upper = dict(
    zip(
      string.ascii_uppercase,
      range(len(string.ascii_uppercase) + 1, (len(string.ascii_uppercase) * 2) + 1),
      strict=True)
  ) 
  priority_lookup = priority_lower | priority_upper
  # print(priority)

  sum_of_priorities = 0
  for rucksack in input:
    compartment_one = rucksack[:len(rucksack)//2]
    compartment_two = rucksack[len(rucksack)//2:]
    # print(compartment_one, compartment_two)

    common = set(compartment_one).intersection(compartment_two).pop()
    # print(common)
    sum_of_priorities += priority_lookup[common]
  
  print(f"The answer to task 1 is: {sum_of_priorities}")

  #---------------------------------------------------------------------------

  split = lambda A, n: [A[i:i+n] for i in range(0, len(A), n)]
  groups = split(input, 3)
  # print(groups)

  sum_of_badge_priorities = 0
  for group in groups:
    rucksacks = [set(x) for x in group]
    badge = set.intersection(*rucksacks).pop()
    # print(f"badge: {badge}")
    sum_of_badge_priorities += priority_lookup[badge]

  print(f"The answer to task 2 is: {sum_of_badge_priorities}")

if __name__ == '__main__':
  main()
