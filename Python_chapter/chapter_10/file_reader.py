filename = 'pi_digits.txt'

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
