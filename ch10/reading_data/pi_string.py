from pathlib import Path

path = Path('pi_digits.txt')
content = path.read_text().rstrip()

lines = content.splitlines()
pi_string = ''
for line in lines:
    #pi_string = pi_string + line
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))
