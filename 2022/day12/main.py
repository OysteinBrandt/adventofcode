import sys
import collections

def to_height(c: chr) -> int:
  if c == 'S':
    return ord('a')
  if c == 'E':
    return ord('z')
  return ord(c)

def bfs(grid, start, goal, width, height):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and (to_height(grid[y][x]) - to_height(grid[y2][x2])) in [-1, 0, 1] and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

def main():
  map = sys.stdin.read().split("\n")
  for row in map:
    print(row)

  for y, row in enumerate(map):
    for x, val in enumerate(row):
      if val == 'S':
        position = (x, y)
  
  path = bfs(map, position, 'E', len(map[0]), len(map))
  print(path)

  for x, y in path:
    map[y] = f"{map[y][:x]}{'x'}{map[y][x+1:]}"
    #for row in map:
    #  print(row)
    #print("-------------------------")
    #time.sleep(2)

  print("------------------------------------")
  for row in map:
    print(row)

def main_test1():
  map = sys.stdin.read().split("\n")
  for row in map:
    print(row)

  for y, row in enumerate(map):
    for x, val in enumerate(row):
      if val == 'S':
        position = [x, y]
      elif val == 'E':
        end_pos = [x, y]

  dirs = {'^': [0, -1], '>': [1, 0], 'v': [0, 1], '<': [-1, 0]}
  current_elevation = 'S'
  path = []
  visited = lambda x,y: any((x == path[i] and y == path[i+1]) for i in range(0, len(path), 3))
  prev_pos = [-1, -1]
  itrs = 0

  while current_elevation != 'E':
    itrs += 1
    desire_x_direction = position[0]-end_pos[0]
    desire_y_direction = position[1]-end_pos[1]
    order = []
    if abs(desire_x_direction) > abs(desire_y_direction):
      if desire_x_direction < 0:
        order += ['>']
      else:
        order += ['<']
      if desire_y_direction < 0:
        order += ['v']
      else:
        order += ['^']
    else:
      if desire_y_direction < 0:
        order += ['v']
      else:
        order += ['^']
      if desire_x_direction < 0:
        order += ['>']
      else:
        order += ['<']
    
    for direction in ['<', '>', 'v', '^']:
      if not direction in order:
        order.append(direction)

    #for d, dir in dirs.items():
    #print(order)
    for d in order:
      check_dir = dirs[d]
      check_pos = [0, 0]
      check_pos[0] = position[0] + check_dir[0]
      check_pos[1] = position[1] + check_dir[1]

      #print("Check pos", check_pos)
      if check_pos[0] < 0 or check_pos[1] < 0: # Prevent map wrapping
        #print(check_pos, "ignored by bounds check 1")
        continue
      if check_pos[0] >= len(map[0]) or check_pos[1] >= len(map):
        #print(check_pos, "ignored by bounds check 2")
        continue

      if check_pos[0] == prev_pos[0] and check_pos[1] == prev_pos[1]:
        #print(check_pos, "ignore previous position")
        continue

      current_char = map[position[1]][position[0]]
      other_char = map[check_pos[1]][check_pos[0]]
      current_h = to_height(current_char)
      other_h = to_height(other_char)

      if visited(check_pos[0], check_pos[1]):
        #print(f"{other_char} at {check_pos} already visited")
        continue

      if (current_h - other_h) in [0, 1, -1]:
        print(f"At position {position} {current_char} choosing {other_char} at {d} with diff {(current_h - other_h)}")
        path += [position[0], position[1], d]
        prev_pos = position
        position = check_pos
        current_elevation = other_char
        #print(current_elevation)
        break
      else:
        print("ignored with diff", current_h-other_h)

    #print(path)
    # NOCOMMIT - REMOVE
    if itrs > 50:
      break

  for i in range(0, len(path), 3):
    x = path[i]
    y = path[i+1]
    d = path[i+2]
    map[y] = f"{map[y][:x]}{d}{map[y][x+1:]}"
    #for row in map:
    #  print(row)
    #print("-------------------------")
    #time.sleep(2)

  print("------------------------------------")
  for row in map:
    print(row)

  print(f"Solution to task 1 is: {itrs}")
  print(f"Also solution to task 1 is: {len(path)//3}")

if __name__ == '__main__':
  main()
