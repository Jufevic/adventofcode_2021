from pathlib import Path

from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

position = 0
depth = 0
aim = 0

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        instruction, steps = parse("{} {:d}", line)
        match instruction:
            case "forward":
                position += steps
                depth += steps * aim
            case "down":
                aim += steps
            case "up":
                aim -= steps

print(depth * position)
