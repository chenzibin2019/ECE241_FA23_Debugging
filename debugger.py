"""
Example: debugger interface
"""

import json


def get_grade(student):
    """
    Get the grade from student object, if no grade record were found, return 0
    :param student: A student object
    :return: The student's grade
    """
    if "grade" in student:
        return student["grade"]
    else:
        return 0


def get_all_grade(students):
    """
    Get a list of all grade from student list
    :param students: The list of student objects
    :return: The list of grades
    """
    all_grades = []
    for student in students:
        grade = get_grade(student)
        all_grades.append(grade)

    return all_grades


def report(students):
    """
    Generate a report of student grades
    :param students: The list of students
    :return: None
    """
    grades = get_all_grade(students)
    avg = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    print(f"The average grade is {avg}, with highest score {highest} and lowest score {lowest}, full mark is 100 points")


if __name__ == "__main__":
    file = open("students.json", "r")
    students = json.load(file)
    report(students)
