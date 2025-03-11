#!/usr/bin/env python3
# Author ID: 143292233

class Student:
    # The __init__ method is called when a new Student object is created.
    # It initializes the student name, number (converted to string), and an empty dictionary for courses.
    def __init__(self, name, number):
        self.name = name  # Assign the student's name to the instance
        self.number = str(number)  # Convert student number to string (to avoid errors with integers)
        self.courses = {}  # Initialize an empty dictionary to hold the courses and grades

    # This method returns the student's name and student number as a formatted string.
    # It allows us to display the student's basic information easily.
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    # The addGrade method allows us to store a new grade for a course.
    # It takes two arguments: course (course name) and grade (the grade the student received).
    # The grade is stored in the self.courses dictionary with the course name as the key.
    def addGrade(self, course, grade):
        self.courses[course] = grade  # Add the course and its grade to the dictionary

    # This method calculates the student's GPA based on the grades of all courses they are enrolled in.
    # If no courses are recorded (i.e., the courses dictionary is empty), we return a GPA of 0.0.
    def displayGPA(self):
        # Check if there are no courses in the dictionary to prevent division by zero
        if len(self.courses) == 0:
            return 'GPA of student ' + self.name + ' is 0.0'  # Return 0.0 if no grades exist
        # Sum all the grades and divide by the number of courses to calculate the GPA
        gpa = sum(self.courses.values())
        return 'GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses))  # Return GPA as a string

    # This method generates a list of courses the student has passed.
    # A course is considered "passed" if its grade is greater than 0.0 (i.e., not a failing grade).
    # It filters out courses with a grade of 0.0.
    def displayCourses(self):
        # Use a list comprehension to filter out courses where the grade is 0.0
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0]
        return passed_courses  # Return the list of passed courses

# The following block of code is executed when the script runs as the main program.
if __name__ == '__main__':
    # Creating the first student object (student1) and adding grades to their record
    student1 = Student('John', '013454900')  # Create a new student with name and student number
    student1.addGrade('uli101', 1.0)  # Add a grade for the 'uli101' course
    student1.addGrade('ops245', 2.0)  # Add a grade for the 'ops245' course
    student1.addGrade('ops445', 3.0)  # Add a grade for the 'ops445' course

    # Creating the second student object (student2) and adding grades
    student2 = Student('Jessica', '123456')  # Create a new student with name and student number
    student2.addGrade('ipc144', 4.0)  # Add a grade for the 'ipc144' course
    student2.addGrade('cpp244', 3.5)  # Add a grade for the 'cpp244' course
    student2.addGrade('cpp344', 0.0)  # Add a grade for the 'cpp344' course (fail)

    # Display the details of student1: name, number, GPA, and passed courses
    print(student1.displayStudent())  # Output student1's name and number
    print(student1.displayGPA())  # Output student1's GPA based on their grades
    print(student1.displayCourses())  # Output the courses student1 has passed (grades > 0.0)

    # Display the details of student2: name, number, GPA, and passed courses
    print(student2.displayStudent())  # Output student2's name and number
    print(student2.displayGPA())  # Output student2's GPA based on their grades
    print(student2.displayCourses())  # Output the courses student2 has passed (grades > 0.0)
