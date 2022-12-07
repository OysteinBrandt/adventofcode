from pathlib import Path

def read_input():
  input_file_path = Path(__file__).parent / 'input.txt'
  # input_file_path = Path(__file__).parent / 'example_input.txt'
  # input_file_path = Path(__file__).parent / 'example_input2.txt'
  # input_file_path = Path(__file__).parent / 'example_input_task2.txt'
  with open(input_file_path, 'r') as file:
    return file.read().splitlines()

def position_at_unique_length(text: str, length: int) -> int:
  for i in range(len(text) - length):
    section = text[i:i + length]
    if len(set(section)) > length - 1:
      return i + length

def main():
  input = read_input()
  line = input[0]

  # The answer to this task was found after multiple social beers xD
  print(f"The answer to task 1 is: {position_at_unique_length(line, 4)}")
  print(f"The answer to task 2 is: {position_at_unique_length(line, 14)}")

if __name__ == '__main__':
  main()
