
#Record structure

#Rachael Graveling
#28/08/2020

# List to store all records
student_records = []

# Number of records
number_of_students = 3

# Loop for each student
for x in range(number_of_students):
    student = []

    student.append(input('Please enter name: '))

    student.append(float(input('Please enter age : ')))
    while student[1] < 1 or student[1] > 150 or not student[1].is_integer():
        print('Error. Must be a whole number between 1 & 150')
        student[1] = float(input('Please enter age : '))

    student[1] = int(student[1])

    student.append(float(input('Please enter height : ')))
    while student[2] < 1 or student[2] > 2.5:
        print('Error. Must be a number between 1 & 2.5')
        student[2] = float(input('Please enter height : '))

    student.append(input('What is your home town?: '))

    # Add the student record to list of records
    student_records.append(student)

# Print the records
for x in student_records:
    print(x)