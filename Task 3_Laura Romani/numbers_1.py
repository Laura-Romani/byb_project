# asking user to enter 3 different integers
number_1 = int(input("Please enter an integer:"))
number_2 = int(input("Please enter a second integer:"))
number_3 = int(input("please enter a third integer:"))

# creating a list of the input integers
number_list = [number_1, number_2, number_3]
print(number_list)

# performing operations requested
print(sum(number_list))
print(number_1 - number_2)
print(number_3 * number_1)
print(int(sum(number_list) / number_3))



