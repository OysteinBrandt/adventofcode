from pathlib import Path
from dataclasses import dataclass
from typing import List
import re

def read_input():
  input_file_path = Path(__file__).parent / 'input.txt'
  # input_file_path = Path(__file__).parent / 'example_input.txt'
  with open(input_file_path, 'r') as file:
    return file.read().splitlines()

MAX_DIR_SIZE = 100_000
TOTAL_DISK_SPACE = 70_000_000
NEED_UNUSED_SPACE = 30_000_000

@dataclass()
class File: # Everything on disk is a file! :) 🎁
  name: str
  size: int
  parent: 'File'
  children: List['File']

def change_dir(name: str, file: File) -> File:
  for child in file.children:
    if child.name == name:
      return child
  raise ValueError(f"'{name}' was not found in any of {[c.name for c in file.children]}")

def print_filesystem(file: File, indent='') -> None:
  type = "dir" if file.children else "file"
  size = f", size={file.size}" if file.size else ""
  print(f"{indent}- {file.name} ({type}{size if size else ''})")
  if not file.children:
    return
  for child in file.children:
    print_filesystem(child, indent + '  ')

def calculate_dir_size(file: File) -> int:
  if file.children:
    file.size = sum([s for s in map(calculate_dir_size, file.children)])
    return file.size
  elif file.size:
    return file.size
  raise Exception(f"Could not calculate file size for '{file.name}'")

def total_size_of_dirs(file: File, dir_max_size: int) -> int:
  result = 0
  if file.children is None:
    return result

  for child in file.children:
    is_dir = bool(child.children)
    if is_dir and child.size <= MAX_DIR_SIZE:
      result += child.size
    result += total_size_of_dirs(child, dir_max_size)
  return result

def find_dir_to_delete(file: File, min_space_to_remove: int) -> File:
  # print(f"to remove: {min_space_to_remove}, checking dir {file.name} with size {file.size}")
  best_match = file
  if file.children is None:
    return None # Files are not included. We are looking to delete a directory.

  for child in file.children:
    _diff = min_space_to_remove - child.size
    if _diff <= 0 and (child.children):
      best_sub_dir = find_dir_to_delete(child, min_space_to_remove)
      if best_sub_dir is not None and best_sub_dir.size < best_match.size:
        best_match = best_sub_dir
      elif best_match is None or child.size < best_match.size:
        best_match = child

  return best_match

def main():
  input = read_input()
  # print(input)
  # print("----------------------------------------------------")

  root = File(name='/', size=None, parent=None, children=[])
  file_pattern = re.compile(r"(\d+) (.*)")
  active_path = None

  # Construct filesystem representation
  i = 0
  while i < len(input):
    if input[i] == '$ ls':
      # print(input[i])
      while i < len(input)-1 and not input[i+1].startswith('$'):
        i += 1
        if input[i].startswith('dir'):
          # print(input[i])
          # print(f"Found folder: {input[i][4:]}")
          active_path.children.append(File(name=input[i][4:], size=None, parent=active_path, children=[]))
          # print(f"Active path: {active_path}")
        else: # file, e.g. "123 file.foo"
          # print(input[i])
          (size, name) = file_pattern.findall(input[i])[0]
          # print(f"Found file with name {name} and size {size}")
          active_path.children.append(File(name=name, size=int(size), parent=active_path, children=None))
    elif input[i].startswith('$ cd'):
      # print(input[i])
      if '/' in input[i]:
        active_path = root
      elif '..' in input[i]:
        active_path = active_path.parent
      else:
        active_path = change_dir(input[i][5:], active_path)
    else:
      raise Exception(f"Unrecognized input: '{input[i]}' at index {i}")
    i += 1

  print("----------------------------------------------------")
  print_filesystem(root)
  print("----------------------------------------------------")
  calculate_dir_size(root)
  print_filesystem(root)
  print("----------------------------------------------------")

  # Find folders of given size and accumulate result
  print(f"The answer to task 1 is: {total_size_of_dirs(root, MAX_DIR_SIZE)}")

  # Find directory to delete
  dir = find_dir_to_delete(root, min_space_to_remove=NEED_UNUSED_SPACE - (TOTAL_DISK_SPACE - root.size))
  print(f"The answer to task 2 is: {dir.size}, with dir name {dir.name}")

if __name__ == '__main__':
  main()
