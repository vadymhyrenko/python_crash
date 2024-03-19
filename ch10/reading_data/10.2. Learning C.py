# message = 'I really like dogs'
# print(message)
#
# message = message.replace('dog', 'cat')
# print(message)
#
# from pathlib import Path
#
# path = Path('learning_python.txt')
# content = path.read_text()
#
# if 'Python' in content:
#     content = content.replace('Python', 'C++')
# print(content)


filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    line = line.rstrip()
    print(line.replace('Python', 'C++'))