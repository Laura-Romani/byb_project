# opening DOB.txt file in reading mode using the with open function
with open("DOB.txt", "r") as file:
# printing the line "Name:" before for loop so it doesnt iterate at every name line
    print("\nName:")
# initiating for loop within the open file function to iterate each name line separately
    for line in file:
# creating a variable to store the name items in a list using the .split method together with (maxsplit=3)
# so that the line divides into at least 3 items
        split_name_birth = line.split(maxsplit=3)
# creating a variable to store teach name as a string, using the .join method to join the two items from the left
#to have a name and surname in a string
        names = " ".join(split_name_birth[0:2])
# printing each name and surname in one line in iteration
        print(names)

# opening DOB.txt file in reading mode using the with open function again for the second part
with open("DOB.txt", "r") as file:
# printing the line "Birthdate:" before for loop again so it doesnt iterate at every name line
    print("\nBirthdate:")
# initiating for loop within the open file function to iterate each name line separately
    for line in file:
# creating a variable to store birthdate items in a list using the .split method together with (maxsplit=3, 
# so that the line divides into at least 3 items
        split_name_birth = line.split(maxsplit=3)
# creating a variable to store each birthdate as a string, using the .join method to join the last two items from the right
#to have a complete date of birth for each name
        birthdates = " ".join(split_name_birth[2:4])
# using the .strip method for the birthdate variable so to eliminate the whitespace in between each line
        birthdates = birthdates.strip()
# printing each birthdate (day month year) in one line in iteration             
        print(birthdates)
