'''
Program Title

A Programmer
01/01/1970

A brief description of what the program does
'''

student = []

student.append(input('Please enter name: '))

student.append(int(input('Please enter age: ')))
while student[1] <1 or student[1] >150:
  print ("Error. Must be between 1 and 150.")
  student.append(int(input('Please enter age: ')))

student.append(float(input('Please enter height: ')))

while student[2] <1 or student[2] >2.5:
  print("Error. Must be between 1 and 2.5.")
  student.append(float(input('Please enter height: ')))

student.append(input('What is your home town?: '))

print(student)