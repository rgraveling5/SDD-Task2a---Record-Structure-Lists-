
#Record structure

#Rachael Graveling
#28/08/2020

student = []

student.append(input('Please enter name: '))

student.append(int(input('Please enter age: ')))
while student[1] <1 or student[1] >150:
  print ("Error. Must be between 1 and 150.")
  student[1] = int(input('Please enter age: '))

student.append(float(input('Please enter height: ')))

while student[2] <1 or student[2] >2.5:
  print("Error. Must be between 1 and 2.5.")
  student[2]= float(input('Please enter height: '))

student.append(input('What is your home town?: '))

print(student)