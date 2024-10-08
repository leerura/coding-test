a = int(input())
b = int(input())

splits = [int(digit) for digit in str(b)]

for split in splits:
    print(a*split)

print(a*b)

