favourite_numbers = {
    'vadym': [8],
    'liubania': [9, 11],
    'vyktor': [4, 12],
    'natalia': [2, 12],
    'viacheslav': [9],
    'valentyna': [7, 4, 5],
}
for k, v in favourite_numbers.items():
    if len(v) > 1:
        print(f"So, {str(k.title())}'s favourite numbers are:")
    else:
        print(f"So, {str(k.title())}'s favourite number is:")
    for number in v:
        print(f"- {str(number)}")
