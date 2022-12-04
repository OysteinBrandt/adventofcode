from pathlib import Path

def read_input():
  # NOTE: It appears that the input might change during the event.
  #       Use website to get latest data before delivering answer.
  input_file_path = Path(__file__).parent / 'input.txt'
  # input_file_path = Path(__file__).parent / 'example_input.txt'
  with open(input_file_path, 'r') as file:
    return file.read().splitlines()

def main():
  input = read_input()
  print(input)

if __name__ == '__main__':
  main()
