split = 'This text contains\n split lines'
#print(split)

no_split = 'This text contains\n split lines'
no_split = no_split.splitlines()
#print(no_split)

for line in no_split:
    print(line)