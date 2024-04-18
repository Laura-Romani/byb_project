# creating an input variable for the number of rows

rows = int(input("How many rows is your pattern? "))
star = "*"

# using a single for loop with range function and nested if/else statement to print stars forward and backward

for i in range(0, rows):
    if i in range (0, 6) :
        print(star * i)
    else:
        print(star * (rows - i))