def timetable(j):
    number = ""
    for column in range(1, j + 1):
        for row in range(1, j + 1):
            number = number + str(row * column) + "\t"
        number = number + "\n"
    return number
userInput = int(input("Please enter a number:"))
print(timetable(userInput))