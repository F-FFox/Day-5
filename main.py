"""fruits = ["Apple", "Peach","Pear"]
for fruit in fruits:
  print (fruit)
#Loops: "for" will assign the variable fruit to each item in the list "Fruits" every time it runs. Therefore the code prints out Apple, then the second time it runs, it prints out peach and the third time it prints out Pear
  print (fruit + " Pie")
"""


"""
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
#print (student_heights)
total_height = 0
number_of_students = 0
for student in student_heights:
  total_height += student
  number_of_students += 1
print (f"total height = {total_height}\nnumber of students = {number_of_students}\naverage height = {int(round((total_height / number_of_students), 0))}")

"""

"""
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highscore = 0
for score in student_scores:
  if score > highscore:
    highscore = score
print(f"The highest score in the class is: {highscore}")

"""

"""
x = 0
for number in range(1, 101):
  x += number
print (x)

"""

"""
add all the even numbers from 1 to a target with a max of 1000

target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
if target > 1000:
  target = 1000
result = 0
for n in range (2, (target + 1), 2):
  result += n
print (result)


# or

# alternative_sum = 0
# for number in range(1, target + 1):
#   if number % 2 == 0:
#     alternative_sum += number
# print(alternative_sum)

"""



"""
for n in range (1 , 101):
  if (n % 3 == 0) and (n % 5 == 0):
    print ("FizzBuzz")
  elif n % 3 == 0:
    print("Fizz")
  elif n % 5 == 0:
    print("Buzz")
  else:
    print(n)

"""