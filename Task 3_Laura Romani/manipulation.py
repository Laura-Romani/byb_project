# asking user to input sentence
str_manip = input("Please enter sencence: ")

# replacing spaces to count characters
str_manip_no_spaces = str_manip.replace(" ", "")

# printing character count in sentence
print(len("The sentence has " + str_manip_no_spaces + " characters."))

# finding last letter in sentence
last_character = str_manip_no_spaces[-1]
print("The last character is: " + last_character)

# replacing every occurrence of last character with @
for character in str_manip:
    if character == last_character:
        str_manip_replaced = str_manip.replace(character, "@")
        print(str_manip_replaced)

# printing last 3 characters of sentence backwords
print("The last three letters backwords are: " + str_manip[:18:-1])

# creating 5-letter word made of first 3 and last 2 characters of sentence
new_string = ((str_manip_no_spaces[0:3]) + (str_manip_no_spaces[-2:]))
print("The new word is: " + new_string)

    



                  