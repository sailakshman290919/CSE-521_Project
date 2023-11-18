import sys

# Define the Student class
class Student:
    def __init__(self, student_id, name, age, gender, contact):
        #Initialize student attributes
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact

    #Display student details
    def display_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Contact: {self.contact}")
        print()

# Define the Course class
class Course:
    def __init__(self, course_code, course_name, max_capacity):
        #Initialize course attributes
        self.course_code = course_code
        self.course_name = course_name
        self.max_capacity = max_capacity
        self.current_enrollment = 0

    #Display course details
    def display_details(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Max Capacity: {self.max_capacity}")
        print(f"Current Enrollment: {self.current_enrollment}")
        print()

# Define the Grade class
class Grade:
    def __init__(self, student, course, grade):
        #Initialize grade attributes
        self.student = student
        self.course = course
        self.grade = grade

    #Display grade details
    def display_details(self):
        print(f"Student: {self.student.name}")
        print(f"Course: {self.course.course_name}")
        print(f"Grade: {self.grade}")
        print()

# Define the CommandParser class
class CommandParser:
    def parse_command(self, user_input):
        #  Parse user input into a list of command components
        return user_input.lower().split()

# Define the UserInterface class
class UserInterface:
    def print_help(self):
        #  Display help message with available commands
        print("Student Information System (SIS)")
        print("Commands:")
        # ... (list of commands)

# Define the EnrollmentSystem class
class EnrollmentSystem:
    def enroll_student(self, student_id, course_code):
        # Enroll a student in a course
        student = next((s for s in student_db.students if s.student_id == student_id), None)
        course = next((c for c in student_db.courses if c.course_code == course_code), None)

        if student and course:
            self.enroll(student, course)
        else:
            print("Invalid student ID or course code.")

    def enroll(self, student, course):
        #Enroll a student in a course and update enrollment count
        if course.current_enrollment < course.max_capacity:
            grade = Grade(student, course, "N/A")
            student_db.add_grade(grade)
            course.current_enrollment += 1
            print(f"{student.name} enrolled in {course.course_name}.")
        else:
            print("Course is full. Enrollment failed.")

    def add_student(self, name, age, gender, contact):
        student_id = len(student_db.students) + 1
        student = Student(student_id, name, age, gender, contact)
        student_db.add_student(student)
        print(f"Student {name} added with ID {student_id}.")

    def add_course(self, course_code, course_name, max_capacity):
        course = Course(course_code, course_name, max_capacity)
        student_db.add_course(course)
        print(f"Course {course_name} added with code {course_code}.")

    def add_grade(self, student_id, course_code, grade):
        student = next((s for s in student_db.students if s.student_id == student_id), None)
        course = next((c for c in student_db.courses if c.course_code == course_code), None)

        if student and course:
            new_grade = Grade(student, course, grade)
            student_db.add_grade(new_grade)
            print(f"Grade added for {student.name} in {course.course_name}.")
        else:
            print("Invalid student ID or course code.")

    def remove_student(self, student_id):
        student = next((s for s in student_db.students if s.student_id == student_id), None)
        if student:
            student_db.remove_student(student)
            print(f"Student {student.name} removed.")
        else:
            print("Invalid student ID.")

    def remove_course(self, course_code):
        course = next((c for c in student_db.courses if c.course_code == course_code), None)
        if course:
            student_db.remove_course(course)
            print(f"Course {course.course_name} removed.")
        else:
            print("Invalid course code.")

# Define the StudentDatabase class
class StudentDatabase:
    def __init__(self):
        self.students = []
        self.courses = []
        self.grades = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def add_grade(self, grade):
        self.grades.append(grade)

    def remove_student(self, student):
        self.students.remove(student)
        self.remove_grades_by_student(student)

    def remove_course(self, course):
        self.courses.remove(course)
        self.remove_grades_by_course(course)

    def remove_grades_by_student(self, student):
        self.grades = [grade for grade in self.grades if grade.student != student]

    def remove_grades_by_course(self, course):
        self.grades = [grade for grade in self.grades if grade.course != course]

    def display_student_details(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                student.display_details()

    def display_course_details(self):
        if not self.courses:
            print("No courses found.")
        else:
            for course in self.courses:
                course.display_details()

    def display_grades(self):
        if not self.grades:
            print("No grades found.")
        else:
            for grade in self.grades:
                grade.display_details()

# Instantiate the student database globally
student_db = StudentDatabase()

# Define the CommandParser class
class CommandParser:
    def parse_command(self, user_input):
        #Parse user input into a list of command components
        return user_input.lower().split()

# Define the UserInterface class
class UserInterface:
    def print_help(self):
        print("Student Information System (SIS)")
        print("Commands:")
        print("  enroll <student_id> <course_code>: Enroll a student in a course")
        print("  add student <name> <age> <gender> <contact>: Add a new student")
        print("  add course <course_code> <course_name> <max_capacity>: Add a new course")
        print("  add grade <student_id> <course_code> <grade>: Add a grade for a student")
        print("  remove student <student_id>: Remove a student")
        print("  remove course <course_code>: Remove a course")
        print("  display students: Display details of all students")
        print("  display courses: Display details of all courses")
        print("  display grades: Display grades of all students")
        print("  help: Display this help message")
        print("  exit: Exit the program")

#Define the main function
def main():
    #Create instances of the classes
    command_parser = CommandParser()
    user_interface = UserInterface()
    enrollment_system = EnrollmentSystem()

    try:
        while True:
            # Get user input
            user_input = input("Enter a command (type 'help' for commands): ")

            if not user_input:
                continue

            #Parse user input and execute corresponding command
            command = command_parser.parse_command(user_input)

            if command[0] == 'enroll' and len(command) == 3:
                #Enroll a student in a course based on user input
                try:
                    student_id = int(command[1])
                    course_code = command[2]
                    enrollment_system.enroll_student(student_id, course_code)
                except ValueError:
                    print("Invalid input. Please enter a valid student ID.")
                except IndexError:
                    print("Invalid input format. Please follow the correct format: enroll <student_id> <course_code>")
                
            elif command[0] == 'add' and len(command) > 3:
                # Process 'add' commands for adding students, courses, or grades
                try:
                    if command[1] == 'student' and len(command) == 6:
                        name, age, gender, contact = command[2], int(command[3]), command[4], command[5]
                        enrollment_system.add_student(name, age, gender, contact)
                    elif command[1] == 'course' and len(command) >= 5:
                        course_code, course_name = command[2], ' '.join(command[3:-1])
                        max_capacity = int(command[-1])
                        enrollment_system.add_course(course_code, course_name, max_capacity)
                    elif command[1] == 'grade' and len(command) == 5:
                        student_id, course_code, grade = int(command[2]), command[3], command[4]
                        enrollment_system.add_grade(student_id, course_code, grade)
                    else:
                        print("Invalid 'add' command or incorrect number of arguments.")
                except ValueError:
                    print("Invalid input. Please check the provided values.")

            elif command[0] == 'remove' and len(command) == 3:
                # Process 'remove' commands for removing students or courses
                try:
                    if command[1] == 'student':
                        student_id = int(command[2])
                        enrollment_system.remove_student(student_id)
                    elif command[1] == 'course':
                        course_code = command[2]
                        enrollment_system.remove_course(course_code)
                    else:
                        print("Invalid 'remove' command. Use 'remove student <student_id>' or 'remove course <course_code>'.")
                except ValueError:
                    print("Invalid input. Please enter a valid student ID or course code.")

            elif command[0] == 'display' and len(command) == 2:
                #Process 'display' commands for displaying student details, course details, or grades
                if command[1] == 'students':
                    student_db.display_student_details()
                elif command[1] == 'courses':
                    student_db.display_course_details()
                elif command[1] == 'grades':
                    student_db.display_grades()
                else:
                    print("Invalid 'display' command. Use 'display students', 'display courses', or 'display grades'.")

            elif command[0] == 'help':
                #Display help message
                user_interface.print_help()

            elif command[0] == 'exit':
                #Exit the program
                print("Exiting the program. Goodbye!")
                sys.exit()

            else:
                #Handle invalid commands
                print("Invalid command. Type 'help' for commands.")

    except SystemExit:
        pass

#Run the main function if the script is executed
if __name__ == "__main__":
    main()
