# ask user name, age, house number and street name
user_name = input("What is your name?")
user_age = input("What is your age?")
user_address = input("What is your house number?") + input( "What is your street name?")
# print all variables in one argument
print(f"Hello, my name is{user_name} and I am{user_age} years old. I live in{user_address}.")