"""Python list comprehension provides a concise, one-line syntax to create a new list from an existing iterable (like a list, tuple, string, or range). It serves as a faster, more "Pythonic" alternative to traditional for loops."""
# doubled_list = [n*2 for n in range(1,6)]
# print(doubled_list)


# Task 
# create a new list with the names with less that 12 letters
random_names = [
    "Liam Smith", "Olivia Johnson", "Noah Williams", "Emma Brown", 
    "Oliver Jones", "Ava Garcia", "Elijah Miller", "Charlotte Davis", 
    "William Rodriguez", "Sophia Martinez", "James Hernandez", "Amelia Lopez", 
    "Benjamin Gonzalez", "Isabella Wilson", "Lucas Anderson", "Mia Thomas"
]

# short_names = [name for name in random_names if len(name) < 12]
# print(short_names)


# Task 
# create a new list with the names with graster that 10 letters and turn them in upper case
random_names = [
    "Liam Smith", "Olivia Johnson", "Noah Williams", "Emma Brown", 
    "Oliver Jones", "Ava Garcia", "Elijah Miller", "Charlotte Davis", 
    "William Rodriguez", "Sophia Martinez", "James Hernandez", "Amelia Lopez", 
    "Benjamin Gonzalez", "Isabella Wilson", "Lucas Anderson", "Mia Thomas"
]

# upper_case_names = [name.upper() for name in random_names if len(name) > 10]
# print(upper_case_names)


# Dictionary comprehension
# Task: create a new dict with student name as key and a rendom number as their marks
import random
student_names = [
    "Liam Smith", "Olivia Johnson", "Noah Williams", "Emma Brown", 
    "Oliver Jones", "Ava Garcia", "Elijah Miller", "Charlotte Davis", 
    "William Rodriguez", "Sophia Martinez", "James Hernandez", "Amelia Lopez", 
    "Benjamin Gonzalez", "Isabella Wilson", "Lucas Anderson", "Mia Thomas"
]

student_marks = {student:random.randint(30,100) for student in student_names}
# print(student_marks)

passed_student = {pass_stu:marks for (pass_stu, marks) in student_marks.items() if marks >= 60 }
# print(passed_student)

# task: create a dict from a sentence
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
# print(result)

# Loop through pandas data frame

import pandas
stu_dict = {
    "student" : ["ron","smith","lola"],
    "marks":[68,89,52]
}

df = pandas.DataFrame(stu_dict)
for (index, row) in df.iterrows():
    # print(index)
    # print(row)
    if row.marks > 55:
        print(row.marks)