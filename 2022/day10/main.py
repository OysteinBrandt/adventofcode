import sys

def main():
  x = 1
  signal_strength_total = 0
  CRT_width, CRT_height = 40, 6
  pixels = ['.' for _ in range(CRT_width * CRT_height)]

  for cycle, line in enumerate(sys.stdin.read().replace(" ", "\n").split()):
    if (cycle+1) % 40 == 20:
      signal_strength_total += (cycle+1) * x

    is_active_pixel = (x - 1) <= cycle % 40 <= (x + 1)
    pixels[cycle] = '#' if is_active_pixel else '.'

    if line not in ['noop', 'addx']:
      x += int(line)

  print(f"The answer to task 1 is: {signal_strength_total}")
  print("The answer to task 2 is:")
  for beam in ["".join(pixels[i:i+40]) for i in range(0, CRT_width*CRT_height, CRT_width)]:
    print(beam)

if __name__ == '__main__':
  main()
