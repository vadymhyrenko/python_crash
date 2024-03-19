from pathlib import Path

path = Path('pi_digits.txt')
content = path.read_text().rstrip()

lines = content.splitlines()
for line in lines:
    print(line)
