# creating placeholder variables to be incremented with a while loop to find average later on

sum = 0
count = 0

# creating a variable to exclude -1 from the sum of number iterations

number_excluded = -1

# using a boleean variable to work with  while loop (could have used while True also?)

input_asked = True

# initiating a while loop which, as long as the value input is not -1, will sum all user value inputs and increment the count by 1; the if/else works where the value input is == -1
# and therefore the loop stops and no more input is required

while input_asked:
    my_number = int(input("Please enter a number: "))
    if my_number != number_excluded:
        sum += my_number
        count += 1
    else:
        input_asked = False

# using an if statement to return the average of the iterations which is true where the user has actually entered input; casting the average valuable as a float as the average
# can be a decimal number
# printing the average using .format method
         
if count > 0:     
    average = float(sum / count)
    print("The average of the values entered (excluding - 1) is {}".format(average))

        






