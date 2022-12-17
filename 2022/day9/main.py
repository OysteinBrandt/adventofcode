import sys

def main():
  knots = [[0, 0] for _ in range(10)]
  visited_positions_unique_task1 = set()     # Unordered unique elements
  visited_positions_unique_task2 = set()     # Unordered unique elements

  for direction, steps in [line.split() for line in sys.stdin.readlines()]:
    for _ in range(int(steps)):
      match direction:
        case 'R': knots[0][0] += 1
        case 'L': knots[0][0] -= 1
        case 'U': knots[0][1] += 1
        case 'D': knots[0][1] -= 1
      
      for i, ((ax, ay), (bx, by)) in enumerate(zip(knots, knots[1:])):
        if abs(ax - bx) > 1 or abs(ay - by) > 1:
          knots[i+1][0] += max(-1, min(ax - bx, 1))
          knots[i+1][1] += max(-1, min(ay - by, 1))

      visited_positions_unique_task1.add(tuple(knots[1]))
      visited_positions_unique_task2.add(tuple(knots[-1]))

  print(f"The answer to task 1 is: {len(visited_positions_unique_task1)}")
  print(f"The answer to task 2 is: {len(visited_positions_unique_task2)}")

if __name__ == '__main__':
  main()
