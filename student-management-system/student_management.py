students = []


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\n----- Student List -----")

    for student in students:
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        print("------------------------")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Thank you for using the Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
