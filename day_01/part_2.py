from pathlib import Path

import numpy as np

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

numbers = np.loadtxt(INPUT_FILE, dtype=int)
groups = np.convolve(numbers, [1, 1, 1], mode="valid")
diffs = np.diff(groups)
print(sum(diffs > 0))
