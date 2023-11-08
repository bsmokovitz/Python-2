def digit_of_life(birthday):
    birthday = str(birthday)
    while len(birthday) > 1:
        birthday = str(sum([int(i) for i in birthday]))
    return birthday

input_birthday = input("Enter your birthday in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY: ")
print(digit_of_life(input_birthday))