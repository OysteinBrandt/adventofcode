import sys, operator, math
from copy import deepcopy
from typing import List

class Monkey:
  modulo = 1
  def __init__(self, input: str) -> None:
    id, items, operation, test, if_t, if_f = input.split("\n")
    self.id = id.split(':')[0]
    self.items = [int(x) for x in items.split(':')[1].split(',')]
    op_map = {'*': operator.mul, '+': operator.add}
    op = operation[23:24]
    op_val = operation[25:]
    self.op = lambda x: op_map[op](x, x if 'old' in op_val else int(op_val))
    self.divisible_by = int(test.split()[-1])
    Monkey.modulo *= self.divisible_by
    self.if_t_id = int(if_t.split()[-1])
    self.if_f_id = int(if_f.split()[-1])
    self.passes = 0

  def round(self, div_by_3: bool) -> List[tuple[int, int]]:
    monkey_throws = []
    for item in self.items:
      self.passes += 1
      worry = self.op(item) // (3 if div_by_3 else 1) % Monkey.modulo
      next_monkey_idx = self.if_t_id if (worry % self.divisible_by == 0) else self.if_f_id
      monkey_throws.append((next_monkey_idx, worry))
    self.items.clear()
    return monkey_throws

def main():
  monkeys = [Monkey(m) for m in sys.stdin.read().strip().split("\n\n")]
  monkeys2 = deepcopy(monkeys)

  for _ in range(20):
    for monkey in monkeys:
      for idx, worry in monkey.round(True):
        monkeys[idx].items.append(worry)

  monkey_business = math.prod(sorted([m.passes for m in monkeys])[-2:])
  print(f"Answer to task 1 is: {monkey_business}")

  for _ in range(10_000):
    for monkey in monkeys2:
      for idx, worry in monkey.round(False):
        # print(f"{monkey.id} throws item with worry {worry} to Monkey {idx}")
        monkeys2[idx].items.append(worry)

  monkey_business = math.prod(sorted([m.passes for m in monkeys2])[-2:])
  print(f"Answer to task 2 is: {monkey_business}")

if __name__ == '__main__':
  main()
