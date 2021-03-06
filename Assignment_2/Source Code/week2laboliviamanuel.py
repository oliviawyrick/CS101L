Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('**** Welcome to the LAB grade calculator! ****')

name = input('Who are we calculating grades for? ==> ')

lab_grade = float(input('Enter the Labs grade? ==> '))
lab_weight = 0.7

if lab_grade > 100:
  lab_grade = 100
  print('The lab value should have been 100 or less. It has been changed to 100')
elif lab_grade < 0:
  lab_grade = 0
  print('The lab value should have been zero or greater. It has been changed to zero')


exam_grade = float(input('Enter the EXAMS grade? ==> '))
exam_weight = 0.2

if exam_grade > 100:
  exam_grade = 100
  print('The exam value should have been 100 or less. It has been changed to 100')
elif exam_grade < 0:
  exam_grade = 0
  print('The exam value should have been zero or greater. It has been changed to zero')


attend = float(input('Enter the Attendance grade? ==> '))
attend_weight = 0.1

if attend > 100:
  attend = 100
  print('The attendance value should have been 100 or less. It has been changed to 100')
elif attend < 0:
  attend = 0
  print('The attendance value should have been zero or greater. It has been changed to zero')


weight_grade = ((lab_grade * lab_weight) + (exam_grade * exam_weight) + (attend * attend_weight))
print('The weighted grade for', name, 'is', round(weight_grade, 2))

if 89 < weight_grade:
  print(name, 'has a letter grade of A')
elif 79 < weight_grade:
  print(name, 'has a letter grade of B')
elif 69 < weight_grade:
  print(name, 'has a letter grade of C')
elif 59 < weight_grade:
  print(name, 'has a letter grade of D')
else:
  print(name, 'has a letter grade of F')

print('**** Thanks for using the Lab grade calculator ****')