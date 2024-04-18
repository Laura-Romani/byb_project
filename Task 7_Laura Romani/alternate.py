# n.2 NEW COMMENT: Apologies I completely misunderstood the task, this is now achieving the wanted result
# using for loops with conditional statements

# creating a string variable
my_string = "Hello my name is Laura."

# storing the number of string characters into a variable to use in the first loop below
character_length = len(my_string)

# using a 'for' conditional statement to loop through each character index, then using a modulus
# to alternate upper case and lower case characters (char)
# using odd and even indexes; range corresponds to the length of characters in the string
# here if a character has an odd index then is lower case, if even is upper case

my_new_string1 = ""
for char in range(character_length):
    if char % 2 == 1:
        my_new_string1 += my_string[char].lower()
    else:
        my_new_string1 += my_string[char].upper()

# using the join function to join the modified characters into a string and printing the string
my_new_string1 = "".join(my_new_string1)
print(my_new_string1)

# using a 'for' conditional statement to loop word index, then using a modulus
# to alternate upper case and lower case characters (char)
# using odd and even indexes; range corresponds to the length of words in the string
# here if a word has an even index then is lower case, if odd is upper case

my_string_words_list = my_string.split()
words_length = len(my_string_words_list)

my_new_string2 = ""
for i in range(words_length):
    if i % 2 == 0:
        my_new_string2 += my_string_words_list[i].lower() + " "
    else:
        my_new_string2 += my_string_words_list[i].upper() + " "

# using the join function to join the modified words into a string and printing the string
my_new_string2 = "".join(my_new_string2)
print(my_new_string2)
