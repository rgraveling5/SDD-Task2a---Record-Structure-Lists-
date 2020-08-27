'''
Program Title

A Programmer
01/01/1970

A brief description of what the program does
'''

student = []

student.append(input('Please enter name: '))

age = int(input("Please enter age: "))
while age <1 or age >1500:
  age = int(input("Please re-enter age: "))
  print()
student.append(age)

height = float(input("Please enter height (m): "))
while height <1 or height > 8.5:
  height = float(input("Please re-enter height(m): "))
  print()
student.append(height)
 
student.append(input('What is your home town?: '))

print()
print(student)