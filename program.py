def add_course():
    # Get course code from user
    course_code = input("Enter the course code: ").upper()

    # Check the length of the course_code
    if len(course_code) != 6:
        print("The length of course codes entered should be 6.")
        add_course()
        return

    # Open course_info.txt 
    with open("/home/course_info.txt", "r") as f:
        lines = f.readlines()

    # Check if the course code already exists in the file
    code_found = any(course_code in line for line in lines)

    # If the code is found, inform the user and prompt for a new one
    if code_found:
        print("This course code exists in our database.")
        add_course()
        return

    # Get the course name from the user
    while True:
        course_name = input("Enter the course name: ")

        # Check if the length of the course is between 1 to 40 characters inclusive
        if len(course_name) < 1 or len(course_name) > 40:
            print("The length of the name should be between 1 and 40 characters inclusive.")
            continue
        # Check if the course name is alphabetical
        elif not course_name.replace(" ", "").isalpha():
            print("The name should be alphabetic")
            continue
        else:
            break

    # Get the credit hours for the course
    while True:
        credit_hours = input("How many credit hours does this course have? ")

        # Check if the credit hours are valid
        if not is_valid_credit_hour(credit_hours):
            continue
        else:
            break

    # Create a new entry for the course
    entry = f"{course_code},{course_name},{credit_hours}\n"

    # Append the course into the the course information file
    with open("/home/course_info.txt", "a") as f:
        f.write(entry)

    print("\n")
    main()


def is_valid_credit_hour(credit_hours):
    try:
        hours = int(credit_hours)

        # Check if the credit hours are between 1 to 5 inclusive
        if 1 <= hours <= 5:
            return True
        else:
            print("The credit hour for each course should be an integer between 1 and 5 inclusive.")
            return False
    except ValueError:
        print("The credit hour for each course should be an integer between 1 and 5 inclusive.")
        return False


def add_student():
    student_id = input("Enter the student ID: ")

    # Check if the student ID entered is 10 characters
    if len(student_id) != 10:
        print("The length of the student ID should be 10 characters.")
        add_student()
        return

    # Open file with the student information
    with open("/home/student_info.txt", "r") as f:
        lines = f.readlines()

    # Check if the student ID is found in the file
    id_found = any(student_id in line for line in lines)

    # If the student ID is found, the user in informed
    if id_found:
        print("The student ID exists in our database.")
        add_student()
        return

    # Get student name from user
    while True:
        student_name = input("Enter the student name: ")

        # Check if student name is between 1 to 40 characters inclusive
        if len(student_name) < 1 or len(student_name) > 40:
            print("The length of the name should be between 1 and 40 characters inclusive.")
            continue

        # Check if name is alpabetic
        elif not student_name.replace(" ", "").isalpha():
            print("The name should be alphabetic")
        else:
            break

    # Get program code from user
    while True:
        program_code = input("Enter the program code: ").upper()

        # Checks if program code is 5 characters
        if len(program_code) != 5:
            print("The length of the program code entered should be 5.")
            continue
        else:
            break

    # Get amount of courses from user
    while True:
        how_many_courses = input("How many courses does this student have? ")

        # Checks the length and if the amount of courses is a digit, if not the user is prompted for a new one
        if not how_many_courses.isdigit() or int(how_many_courses) < 1 or int(how_many_courses) > 5:
            print("The length of the program code entered should be 5.")
            continue
        else:
            break

    how_many_courses = int(how_many_courses)
    courses = []

    # Get course codes and scores for each course from user
    i = 1
    while i <= how_many_courses:
        course_code = input(f"Enter course code {i}: ").upper()

        # Read course info from file
        with open("/home/course_info.txt", "r") as f:
        # Check if course code exists in course_info.txt file
            if not any(course_code in line for line in f):
                print("This course does not exist in our database.")
                continue

        # Check for duplicate course code and prompts user for a new one
        if any(course_code in course for course in courses):
            print("This course has been entered before.")
            continue
        while True:
            score = input("Enter the student's score for this course: ")

            # Check if the score if valid
            try:
                score = float(score)
            except ValueError:
                print("Score should be a float value.")
                continue
            if score < 0 or score > 100:
                print("The score for each course should be in the range of 0 to 100.")
                continue
            else:
                break

        courses.append((course_code, float(score)))
        i += 1

    # Append student details to student_info.txt file
    with open("/home/student_info.txt", "a") as f:
        f.write(f"{student_id},{student_name},{program_code},")
        f.write(",".join([f"{course}:{score}" for course, score in courses]))
        f.write("\n")
    print("")

    main()

def add_teacher():
    # Get Staff ID from user
    staff_id = input("Enter the staff ID: ")

    # Check if staff ID has 7 characters
    if len(staff_id) != 7:
        print("The length of the staff ID should be 7 characters.")
        add_teacher()
        return

    # Open file with teacher information
    with open("/home/teacher_info.txt", "r") as f:
        lines = f.readlines()

    # Check if the staff ID already exists
    id_found = any(staff_id in line for line in lines)

    # If the staff ID is found, inform the user and prompt for a new staff ID
    if id_found:
        print("The staff ID exists in our database.")
        add_teacher()
        return

    # Get teacher name from user
    while True:
        teacher_name = input("Enter the teacher name: ")
        
        # Check if the length of the name is betweem 1 to 40 characters inclusive
        if len(teacher_name) < 1 or len(teacher_name) > 40:
            print("The length of the name should be between 1 and 40 characters inclusive.")
            continue
        # Checks if the name is alphabetic
        elif not teacher_name.replace(" ", "").isalpha():
            print("The name should be alphabetic.")
            continue
        else:
            break

    # Get number of couses taught by this teacher from the user
    while True:
        how_many_courses = input("How many courses does this teacher teach? ")

        # Checks if the amount of courses is a digit from 1 to 5 inclusive
        if not how_many_courses.isdigit() or int(how_many_courses) < 1 or int(how_many_courses) > 5:
            print("The length of the program code entered should be 5.")
            continue
        else:
            break

    how_many_courses = int(how_many_courses)
    courses = []
    i = 1
    while i <= how_many_courses:
        course_code = input(f"Enter course code {i}: ").upper()

        # Check if course code exists in course_info.txt file
        with open("/home/course_info.txt", "r") as f:  # Read course info from file
            if not any(course_code in line for line in f):
                print("This course does not exist in our database.")
                continue

        # Check for duplicate course code
        if any(course_code in course for course in courses):
            print("This course has been entered before.")
            continue
        
        courses.append(course_code)
        i += 1


    # Append teacher details to teacher_info.txt file
    with open("/home/teacher_info.txt", "a") as f:
        f.write(f"{staff_id},{teacher_name},")
        f.write(",".join(courses))
        f.write("\n")

    print("")

    main()


def student_gpa(course_scores):
    # Open course information file
    with open("/home/course_info.txt", "r") as f: 
        course_info = f.readlines()
    
    # Create a dictionary to store credit hours for every course
    credit_hours = {}
    for line in course_info:
        course_code, course_name, hours = line.strip().split(",")
        credit_hours[course_code] = round(float(hours))

    # Function calculates the GPA
    def calculategpa(course_scores, total_credits = 0, total_points = 0):

        # Base case - no more courses to process
        if not course_scores:
            return total_points / total_credits

        # Get the fist course and its score
        course_code, score = course_scores.pop(0)
        score = int(score)

        # Determine the grade based on the score
        if 80 <= score <= 100:
            grade = 4.00
        elif 75 <= score < 80:
            grade = 3.67
        elif 70 <= score < 75:
            grade = 3.33
        elif 65 <= score < 70:
            grade = 3.00
        elif 60 <= score < 65:
            grade = 2.67
        elif 55 <= score < 60:
            grade = 2.33
        elif 50 <= score < 55:
            grade = 2.00
        elif 47 <= score < 50:
            grade = 1.67
        elif 44 <= score < 47:
            grade = 1.33
        elif 40 <= score < 44:
            grade = 1.00
        else:
            grade = 0.00

        # Calculate points for this course and add to total points
        points = grade * credit_hours[course_code]
        total_points += points

        # Add credit hours for this course to total credits
        total_credits += credit_hours[course_code]

        # Recursively call the function with the remaining courses
        return calculategpa(course_scores, total_credits, total_points)

    return calculategpa(course_scores)

def list_students():
    # Open the file with the course information
    with open("/home/course_info.txt", "r") as f: 
        course_info = f.readlines()

    # Create a dictionary to store credit for every course
    credit_hours = {}
    for line in course_info:
        course_code, course_name, hours = line.strip().split(",")
        credit_hours[course_code] = round(float(hours))

    # Open the file with the student information
    with open("/home/student_info.txt", "r") as f:
        student_info = f.readlines()

    # Iterate over each student in the file
    for line in student_info:
        student_id, student_name, program_code, *courses = line.strip().split(",")
        print(f"Student ID: {student_id}")
        print(f"Student Name: {student_name}")
        print(f"Program Code: {program_code}")
        print("Course    Credit Hour    Score")

        course_scores = []

        # Iterate over every course for the student
        for course in courses:
            course_code, score = course.split(":")
            score = float(score)
            course_scores.append((course_code, score))
            print(f'{course_code}         {credit_hours[course_code]}           {score:.1f}')
        
        # Calculate GPA fopr the student
        gpa = student_gpa(course_scores)
        print(f"GPA is {gpa:.2f}\n")
    main()

def list_teachers():
    # Open the file with the course information
    with open("/home/course_info.txt", "r") as f:
        course_info = f.readlines()
    
    # Create a dictionary to store course names for every course
    course_names = {}
    for line in course_info:
        course_code, course_name, hours = line.strip().split(",")
        course_names[course_code] = course_name

    # Open the file with the teacher information
    with open("/home/teacher_info.txt", "r") as f:
        teacher_info = f.readlines()

        # Iterate over each teacher in the file
        for line in teacher_info:
            staff_id, teacher_name, *courses = line.strip().split(",")
            print(f"Staff ID: {staff_id}")
            print(f"Teacher name: {teacher_name}")
            print("Teaches the following courses: ")

            # Iterate over each course taught by the teacher
            for course_code in courses:
                course_name = course_names[course_code]
                print(f"{course_code}: {course_name}")
            print()
        main()

def search_student():
    # Open the file with the course information
    with open("/home/course_info.txt", "r") as f:
        course_info = f.readlines()
    
    # Create a dictionary to store the credit hours of every course
    credit_hours = {}
    for line in course_info:
        course_code, course_name, hours = line.strip().split(",")
        credit_hours[course_code] = int(hours)
    
    # Prompt the user to choose the search criteria
    print("Search students based on: ")
    print("Select 1 for ID")
    print("Select 2 for Name")
    choice = input("Enter your choice: ")


    while True:

        # Get search ID or name from the user based on their choice
        if choice == "1":
            search_id = input("Enter student ID: ")
        elif choice == "2":
            search_name = input("Enter student name: ")

        # Open the file with the student information
        found = False
        with open("/home/student_info.txt", "r") as f:
            student_info = f.readlines()

        # Itera over each student in the file
        for line in student_info:
            student_id, student_name, program_code, *courses = line.strip().split(",")

            # Check if the student matches the search criteria
            if (choice == "1" and student_id == search_id) or (choice == "2" and student_name == search_name):
                found = True
                print(f"Student ID: {student_id}")
                print(f"Student Name: {student_name}")
                print(f"Program Code: {program_code}")
                print("Course    Credit Hour    Score")

                # Calculate GPA
                course_scores = []
                for course in courses:
                    course_code, score = course.split(":")
                    score = float(score)
                    course_scores.append((course_code, score))
                    print(f'{course_code}         {credit_hours[course_code]}           {score:.1f}')
                gpa = student_gpa(course_scores)
                print(f"GPA is {gpa:.2f}\n")
                break
            else:
                print("Student ID/name does not exist in our database.\n")
                continue
        if found:
            main()

def list_teachers_courses():
    # Open the file with the course information
    with open("/home/course_info.txt", "r") as f:
        course_info = f.readlines()

    # Create a dictionary to store course names for very course code
    course_names = {}
    for line in course_info:
        course_code, course_name, hours = line.strip().split(",")
        course_names[course_code] = course_name

    # Open the file with the teacher information
    with open("/home/teacher_info.txt", "r") as f:
        teacher_info = f.readlines()
    
    # Create a dictionary to store teacher names for every course code
    teachers = {}
    for line in teacher_info:
        staff_id, teacher_name, *courses = line.strip().split(",")
        for course_code in courses:
            if course_code not in teachers:
                teachers[course_code] =[]
            teachers[course_code].append(teacher_name)

    while True:
        # Prompt user for student ID
        search_id = input("Enter student ID: ")

        # Open the file with the student information
        found = False
        with open("/home/student_info.txt", "r") as f:
            student_info = f.readlines()
        
        # Iterate over each student in the file
        for line in student_info:
            student_id, student_name, program_code, *courses = line.strip().split(",")
            
            # Check if student matches the search criteria
            if student_id == search_id:
                found = True

                # Iterate over each course for the student
                for course in courses:
                    course_code, grade = course.split(":")

                    # Get the name of the course from the dictionary
                    course_name = course_names[course_code]

                    # Check if there are any teachers for this course code in the dictionary
                    if course_code in teachers:
                        for teacher_name in teachers[course_code]:
                            print(f"Teacher Name: {teacher_name}")
                            print(f"Course Name: {course_names[course_code]}\n")
                    else:
                        print(f"Course Name: {course_names[course_code]}")
                        print(f"The teacher for this course is not specfied.\n")
        if found:
            break
        else:
            print("This student ID does not exist in our database.")
            continue
        
    main()

def course_gpa():
    while True:
        # Prompt user for course code
        search_code = input("Enter the course code: ").upper()

        # open the file with the student information
        found = False
        total_score = 0
        count = 0
        with open("/home/student_info.txt", "r") as f:
            student_info = f.readlines()
        
        # Iterate over each student in the file
        for line in student_info:
            student_id, student_name, program_code, *courses = line.strip().split(",")
            
            # Iterate over each course for the student
            for course in courses:
                course_code, score = course.split(":")

                # Check the course code matches the search criteria
                if course_code == search_code:
                    found = True
                    try:
                        total_score += float(score)
                        count += 1
                    except ValueError:
                        print("Score should be a float value")
        
        if found:
            # Calculate average score and GPA for this course
            avg_score = total_score / count
            gpa = student_gpa([(search_code, avg_score)])
            print(f"GPA for this course is {gpa:.2f}\n")
            break
        else:
            print("This course code does not exist in our database.")
            continue
    
    main()


def main():
    while True:
        print('''Main Menu
Choose any of these options:
1. Add a course
2. Add a student 
3. Add a teacher
4. List all students
5. List all teachers 
6. Search for a student by their name or student ID
7. List the teachers and their courses for a student
8. Show the GPA of a course
Enter zero to exit the program.''')

        # Get user choice from input
        choice = input("Enter your choice: ")

        # Call the appropriate function based on the user's choice
        if choice == "0":
            print("Exiting the program...")
            quit()
        elif choice == "1":
            add_course()
        elif choice == "2":
            add_student()
        elif choice == "3":
            add_teacher()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_teachers()
        elif choice == "6":
            search_student()
        elif choice == "7":
            list_teachers_courses()
        elif choice == "8":
            course_gpa()
        else:
            print("Wrong menu selection.\n")


if __name__ == "__main__":
    main()
