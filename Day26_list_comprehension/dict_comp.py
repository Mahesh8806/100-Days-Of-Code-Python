# Creating a Dectionary from list...
import random
names = ["Mahesh","Rahul","Varsha","Anuja","Karan","Rohit"]
student_scores = {student:random.randint(1,100) for student in names}

print(student_scores)
passed_student = {student : score for (student,score) in student_scores.items() if score > 60}

print(passed_student)

