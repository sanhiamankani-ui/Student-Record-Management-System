import csv
import json
import os

CSV_FILE = "students.csv"
JSON_FILE = "students.json"


# Load student records from CSV
def load_csv():
    students = []

    if os.path.exists(CSV_FILE):
        try:
            with open(CSV_FILE, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    row["Age"] = int(row["Age"])
                    row["Marks"] = float(row["Marks"])
                    students.append(row)

        except (ValueError, KeyError, OSError) as error:
            print("Error reading CSV:", error)

    return students


# Save student records to CSV
def save_csv(students):
    try:
        with open(CSV_FILE, "w", newline="") as file:
            fieldnames = ["ID", "Name", "Age", "Course", "Marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(students)

    except OSError as error:
        print("Error saving CSV:", error)


# Save student records to JSON
def save_json(students):
    try:
        with open(JSON_FILE, "w") as file:
            json.dump(students, file, indent=4)

    except OSError as error:
        print("Error saving JSON:", error)


# Load student records from JSON
def load_json():
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r") as file:
                return json.load(file)

        except (json.JSONDecodeError, OSError) as error:
            print("Error reading JSON:", error)

    return []


# Add a new student
def add_student(students):
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["ID"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Name: ")

    try:
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        if age <= 0 or not 0 <= marks <= 100:
            print("Enter a valid age and marks between 0 and 100.")
            return

    except ValueError:
        print("Please enter numbers for age and marks.")
        return

    course = input("Enter Course: ")

    new_student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }

    students.append(new_student)
    save_csv(students)
    save_json(students)

    print("Student added successfully!")


# Display all students
def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")

    for student in students:
        print(student)


# Search for a student
def search_student(students):
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["ID"] == student_id:
            print("Student Found:", student)
            return

    print("Student not found.")


# Update student information
def update_student(students):
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["ID"] == student_id:
            student["Name"] = input("Enter New Name: ")

            try:
                age = int(input("Enter New Age: "))
                marks = float(input("Enter New Marks: "))

                if age <= 0 or not 0 <= marks <= 100:
                    print("Invalid age or marks.")
                    return

                student["Age"] = age
                student["Marks"] = marks

            except ValueError:
                print("Please enter valid numbers.")
                return

            student["Course"] = input("Enter New Course: ")

            save_csv(students)
            save_json(students)

            print("Student updated successfully!")
            return

    print("Student not found.")


# Delete a student
def delete_student(students):
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)

            save_csv(students)
            save_json(students)

            print("Student deleted successfully!")
            return

    print("Student not found.")


# Show students with marks above 80
def show_top_students(students):
    top_students = list(
        filter(lambda student: student["Marks"] > 80, students)
    )

    print("\n--- Students with Marks Above 80 ---")

    for student in top_students:
        print(student)


# Main program
def main():
    students = load_csv()

    while True:
        print("\n===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Top Students")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student(students)

            elif choice == 2:
                view_students(students)

            elif choice == 3:
                search_student(students)

            elif choice == 4:
                update_student(students)

            elif choice == 5:
                delete_student(students)

            elif choice == 6:
                show_top_students(students)

            elif choice == 7:
                print("Thank you for using the system!")
                break

            else:
                print("Invalid choice. Please select 1 to 7.")

        except ValueError:
            print("Please enter a number.")


if __name__ == "__main__":
    main()
