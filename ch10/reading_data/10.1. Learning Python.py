from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()
print("--- Reading in the entire file:")
print(content)

split_lines = path.read_text().splitlines()

print("\n--- Looping over the lines:")
for line in split_lines:
    print(line)
