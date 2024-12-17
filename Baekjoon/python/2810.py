n = int(input())
seat = input()
number = len(seat)

seat = seat.replace("LL", "l")

cup = len(seat) + 1

if number < cup:
    print(number)
else:
    print(cup)
