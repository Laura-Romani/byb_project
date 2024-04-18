# creating a variable to store number of students using an input from the user and using the try/except to error-validate input value (integer)
while True:
    try:
        number_students = int(input("Please write how many students are registering: "))
# in this loop if the input is entered as an integer the loop will break
        break
# whilst if the input entered is a string or symbol the loop will print the message below, and continue asking the user for input
    except ValueError:
        print("Please enter a valid integer.")

# creating a file called reg_form.txt to store the student IDs
with open("reg_form.txt", "w") as registration_file:
# using the for loop with the number of students value entered by user prior, iterating through each student and asking for student ID
    for i in range(number_students):
        student_id = input(f"Student {i+1} ID number: ")
# using the .write method to write in the reg_form.txt each student ID number followed by a dotted line below the student ID (. times 30)
        registration_file.write(f"Student ID: {student_id}\n")
        registration_file.write("." * 30 + "\n")
# when file is closed, printing message for user to confirm the registration form was created successfully
print("The registration form was created in reg_file.txt")

